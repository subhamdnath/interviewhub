from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):

    def create_user(self, email, full_name, username, phone_number, gender, password):

        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            email=self.normalize_email(email), full_name = full_name,
            username = username, phone_number = phone_number, 
            gender = gender)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, username, phone_number, gender, password):

        user = self.create_user(email, full_name = full_name,
            username = username, phone_number = phone_number,
             gender = gender, password = password)
        
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):

    email = models.EmailField(verbose_name="email_address", max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    gender = models.CharField(max_length=20, default= "Prefer not to say", 
                              choices=(("Male", "Male"), ("Female", "Female"),
                                    ("Prefer not to say","Prefer not to say")))
  
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    def __str__(self):
        return f"{self.email}-{self.username}"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "username", "phone_number", "gender"]


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = "MyUser"
            