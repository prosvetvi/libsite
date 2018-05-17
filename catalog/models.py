from django.db import models
from django.contrib.auth.models import User
import uuid


class Author(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    birth_date = models.DateTimeField('date birthday')

    def __str__(self):
        return u'%s %s' % (self.name, self.surname)


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    read_date = models.DateTimeField('date reading')
    authors = models.ManyToManyField(Author)
    image = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class BookReading(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_last_read = models.DateField()
