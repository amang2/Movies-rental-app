from django.contrib.auth.base_user import BaseUserManager
import uuid

class UserManager(BaseUserManager):
    def create_user(self, username, password,phone_no,**extra_fields):
        
        if not username:
            raise ValueError('You must provide an username address.')
        if not phone_no:
            raise ValueError('You must provide an phone no.')
        user = self.model(username=username,phone_no=phone_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

   
    def create_superuser(self, username, password,phone_no, **extra_fields):
        """
        Creates and saves a superuser with the given username and password.
        """
        extra_fields.setdefault("public_id", uuid.uuid4().int >> 75)
        user = self.create_user(
            username, password,phone_no, **extra_fields
        )
        user.staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

