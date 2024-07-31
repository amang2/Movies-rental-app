from users.manager import UserManager
from django.db import models
from db.base_model import BaseModel
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin)
from db.base_model import BaseModel

class UserProfile(BaseModel,AbstractBaseUser,PermissionsMixin):
    phone_no = models.CharField(max_length=15, unique=True,null=False, blank=False)
    username = models.CharField(max_length=100,unique=True)
    user_type = models.CharField(max_length=255, default="Customer")
    staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=255, null=True, blank=True)
    # is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_no']

    objects = UserManager()

    class Meta:
        ordering = ('-id',)

    def get_full_name(self):
        # The user is identified by their username address
        return self.username

    def get_short_name(self):
        # The user is identified by their username address
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    # @property
    # def is_superuser(self):
    #     "Is the user a superuser member?"
    #     return self.is_superuser
