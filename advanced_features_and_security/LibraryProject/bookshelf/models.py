# LibraryProject/bookshelf/models.py
"""
Permissions and Groups Setup:

- Custom permissions added to Book model: can_view, can_create, can_edit, can_delete
- Groups created: Editors, Viewers, Admins
    * Editors: can_create, can_edit
    * Viewers: can_view
    * Admins: can_view, can_create, can_edit, can_delete
- Views are protected using @permission_required decorator to enforce these permissions.
"""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from django.conf import settings

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        if not username:
            raise ValueError("The Username field is required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, date_of_birth, profile_photo, **extra_fields)

# Custom User Model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('relationship_app.Author', on_delete=models.CASCADE)
    publication_year = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return self.title