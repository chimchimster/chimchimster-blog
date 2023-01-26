from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy

class UserManager(BaseUserManager):
    """
    Custom model which provides unique identifier via email for authentication
    instead of using "username" field.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save user with email and password.
        """
        if not email:
            raise ValueError(gettext_lazy("Email must be provided"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save superuser with email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields.get("is_staff"):
            raise ValueError(gettext_lazy("Superuser must have is_staff=True"))
        if not extra_fields.get("is_superuser"):
            raise ValueError(gettext_lazy("Superuser must have is_superuser=True"))

        return self.create_user(email, password, **extra_fields)