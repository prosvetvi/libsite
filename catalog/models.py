import os

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.cache import cache

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


class Author(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return u'%s %s' % (self.name, self.surname)


def file_size(value):  # add this to some file where you can import it from
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MiB.')


def get_upload_path_book(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (os.path.splitext(filename)[0] + "_" + str(instance.uuid), ext)
    return os.path.join('files/' + str(instance.author) + "/", filename)


class Book(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,
                            help_text="Unique ID for this particular book across whole library")
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=now())
    read_date = models.DateTimeField('date reading')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True, validators=[file_size], upload_to=get_upload_path_book)
    can_download = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# method for updating cache
@receiver(post_save, sender=Book)
def update_cache(sender, instance, **kwargs):
    cache.set('last_book_list', Book.objects.order_by('-read_date')[:3])


@receiver(models.signals.post_delete, sender=Book)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Book` object is deleted.
    """
    cache.set('last_book_list', Book.objects.order_by('-read_date')[:3])
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


@receiver(models.signals.pre_save, sender=Book)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Book` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Book.objects.get(pk=instance.pk).file
    except Book.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class BookReading(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_last_read = models.DateTimeField('time last reading')
