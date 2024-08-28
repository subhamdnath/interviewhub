from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):

    def create_user(self, full_name, email, phone_number, state, gender, role, password):

        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            email=self.normalize_email(email), full_name = full_name,
             phone_number = phone_number, 
            state = state, gender = gender, role = role
           )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, email, phone_number, state, gender, role, password):

        user = self.create_user(full_name = full_name,
            email = email, phone_number = phone_number, 
            state = state, gender = gender, role = role,
            password = password)
        
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

INDIAN_STATES_AND_UTS = (
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
)



GENDER_CHOICES = (("Male", "Male"), 
                ("Female", "Female"),
                ('Other','Other'),
                ("Prefer not to say","Prefer not to say"))

ROLE_CHOICES = (("Candidate", "Candidate"),
                ("Employer", "Employer"),
                ("Admin", "Admin"))


class MyUser(AbstractBaseUser):

    full_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(verbose_name="email_address", max_length=255, unique=True)
    phone_number = models.CharField(max_length=15)
    state = models.CharField(max_length=50, choices=INDIAN_STATES_AND_UTS,)
    gender = models.CharField(max_length=20, default= "Prefer not to say", choices=GENDER_CHOICES) 
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Candidate")

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    def __str__(self):
        return f"{self.email}-{self.role}"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "phone_number", "state", "gender", "role"]


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = "MyUser"
            
