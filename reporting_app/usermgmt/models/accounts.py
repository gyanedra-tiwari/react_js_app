import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from taggit.managers import TaggableManager

class User(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        help_text="A unique number to identify the user",
        primary_key=True
    )
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    


class Profile(models.Model):

    first_name = models.CharField(
        max_length=20,
        default=None,
        null=True
    )
    last_name = models.CharField(
        max_length=20,
        default=None,
        null=True
    )
    email_init = models.EmailField(
        verbose_name='Initial Email Address',
        null=True
    )
    phone = models.CharField(
        null=True,
        max_length=30
    )
    date_of_birth = models.DateField(null=True)
    address = models.TextField(null=True)
    photo_url = models.URLField(default=None, null=True, help_text="An optional image of the user")
    alternate_phone = models.CharField(
        max_length=15,
        null=True,
    )
    locality = models.TextField(
        help_text="Verbose location of the user",
        default=None,
        null=True
    )
    city = models.CharField(
        max_length=20,
        default=None,
        null=True
    )
    preferred_languages = ArrayField(
        models.CharField(max_length=5),
        default=None,
        null=True,
        help_text="Language codes of preferred languages in the order of preference"
    )
    countries = ArrayField(
        models.CharField(max_length=20),
        default=None,
        null=True
    )
    country_of_origin = models.CharField(
        default=None,
        max_length=20,
        null=True
    )
    current_timezone = models.CharField(
        default=None,
        max_length=20,
        null=True
    )
    timezones = ArrayField(
        models.CharField(max_length=20),
        default=None,
        null=True
    )
    birthday = models.DateField(default=None, null=True)
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name="profile",
        db_index=True,
    )
    contacts = models.ManyToManyField(
        User,
        help_text="Users a user has contact on this platform",
        related_name="friends",
        default=None,
    )