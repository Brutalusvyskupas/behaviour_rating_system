import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class UserAccountManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(_("You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserWorkOffice(models.Model):
    office_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=30, unique=True)
    # office_pic

    def save(self, *args, **kwargs):
        self.slug = slugify(self.office_name)
        super(UserWorkOffice, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'office'
        verbose_name_plural = 'offices'

    def __str__(self):
        return self.office_name

    def get_absolute_url(self):
        return reverse('users:list_of_users_by_office', args=[self.slug])


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4, editable=False, unique=True)
    work_office = models.ForeignKey(
        UserWorkOffice, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='untitled')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address_line = models.CharField(max_length=100, blank=True)
    town_city = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # profile_picture
    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' | ' + self.email

    def get_absolute_url(self):
        return reverse('users:user_details', kwargs={
            'pk': self.pk
        })
