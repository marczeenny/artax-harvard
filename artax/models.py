from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import EmailValidator
from dirtyfields import DirtyFieldsMixin
import os
import functools


def custom_cover_filename(instance, filename, object):
    _, file_extension = os.path.splitext(filename)
    book_id = Book.objects.all().last().pk
    if book_id is None:
        book_id = 0
    filename = f"{instance.id if instance.id is not None else book_id + 1}-{object}{file_extension}"
    return f"{object}/{filename}"


class User(AbstractUser):
    email = models.EmailField(blank=True, unique=True, validators=[EmailValidator(
        message="Please enter a valid email address.")])
    about = models.TextField()
    job = models.CharField(max_length=200)
    address = models.TextField()
    phone = PhoneNumberField(null=True, region="LB")
    date_of_registration = models.DateField(default=datetime.today)
    twitter_url = models.URLField(default="#")
    facebook_url = models.URLField(default="#")
    insta_url = models.URLField(default="#")
    linkedin_url = models.URLField(default="#")

    def __str__(self):
        return f"@{self.username}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


class Book(models.Model, DirtyFieldsMixin):
    lib_id = models.CharField(max_length=50, default="ABC123")
    author = models.ForeignKey("Author", models.PROTECT, related_name="book")
    title = models.CharField(max_length=250)
    subject = models.TextField(null=True)
    type = models.ForeignKey("Type", models.PROTECT, related_name="book")
    section = models.CharField(max_length=250)
    location = models.ForeignKey("Location", models.PROTECT, related_name="book", null=True)
    publisher = models.CharField(max_length=250)
    publishing_date = models.CharField(max_length=250, null=True)
    purchase_date = models.DateField(null=True, blank=True)
    summary = models.FileField(upload_to=functools.partial(custom_cover_filename, object="summary"), blank=True, null=True)
    cover = models.ImageField(upload_to=functools.partial(custom_cover_filename, object="cover"), blank=True, null=True)
    isbn = models.CharField(max_length=14, blank=True, null=True)
    number_of_copies = models.IntegerField()
    language = models.ForeignKey("Language", models.SET_NULL, related_name="book", null=True)
    date_of_registration = models.DateField(default=datetime.today)
    registrator = models.ForeignKey(User, models.SET_NULL, null=True, related_name="book_registrator")
    last_editor = models.ForeignKey(User, models.SET_NULL, null=True, related_name="book_latest_editor")
    last_edit_time = models.DateTimeField()

    def __str__(self):
        return f"{self.title} by {self.author}"


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Type(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} | Code: {self.code}"


class Location(models.Model):
    code = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.code}"


class Language(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} | Code: {self.code}"
