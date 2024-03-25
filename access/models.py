from django.db import models

from common.models import AbstractModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, password, **kwargs):
        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password, **kwargs):
        kwargs["is_admin"] = False
        return self._create_user(password, **kwargs)

    def create_superuser(self, password, **kwargs):
        kwargs["is_admin"] = True
        return self._create_user(password, **kwargs)


class User(AbstractModel, AbstractBaseUser):

    email = models.EmailField(
        max_length=125,
        unique=True,
        db_index=True,
    )

    name = models.CharField(max_length=64, blank=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(
        default=True,
    )
    is_admin = models.BooleanField(
        default=False,
    )

    bio = models.TextField(blank=True)

    USERNAME_FIELD = "email"

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_active and self.is_admin

    def has_module_perms(self, app_label):
        return self.is_active and self.is_admin

    def get_all_permissions(self, obj=None):
        return []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
