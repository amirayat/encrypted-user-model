from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from encrypted_model_fields.fields import EncryptedCharField, EncryptedEmailField
from hashid_field import HashidAutoField


class CustomUserModel(AbstractUser):
    """
    encrypted user model
    """

    username_validator = UnicodeUsernameValidator()

    id = HashidAutoField(primary_key=True)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = EncryptedCharField(
        _("first name"), max_length=150, blank=True)
    last_name = EncryptedCharField(_("last name"), max_length=150, blank=True)
    email = EncryptedEmailField(_("email address"), blank=True, unique=True)
    phone = EncryptedCharField(_("mobile phone"), max_length=13)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "encrypted_users"
