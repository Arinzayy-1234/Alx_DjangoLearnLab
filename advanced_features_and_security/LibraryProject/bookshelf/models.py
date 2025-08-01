from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Permission


# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()

    class Meta:

        permissions = [
            ('can_view', 'Can view objects'),
            ('can_create', 'Can create objects'),
            ('can_edit', 'Can edit objects'),
            ('can_delete ','Can delete objects'),
        ]    
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


    def __str__(self):
        return f'BookID {self.id} Book: {self.title}, Author: {self.author}, Year: {self.publication_year}'

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None,**extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(username,email,password, **extra_fields)




class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile/photos', null= True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
