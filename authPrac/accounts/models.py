from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

class CustomUserManage(BaseUserManager):

    def create_user(self,email,first_name,last_name,username,password=None):
        if not email:
            raise ValueError('Email is must!')

        email=email.lower()
        first_name=first_name
        last_name=last_name
        username=username
        # password=password

        user = self.model(

            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username
            # password=password

        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,first_name,last_name,password=None):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        user.is_admin= True
        user.is_staff=True
        user.save(using=self._db)


    
class CustomUser(AbstractBaseUser):

    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=150,unique=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=True)
    is_writer=models.BooleanField(default=False)
    is_editor=models.BooleanField(default=False)
    last_login=models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)  
    
    is_staff=models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name','last_name')

    objects = CustomUserManage()

    def __str__(self):
        return self.email
    
    def get_short_name(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name_plural = 'Users'