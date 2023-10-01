from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin,
)
from django.urls import reverse_lazy
from django.utils import timezone
import uuid
from django.contrib.auth import get_user_model
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Eメールが必要です!')
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class LoginUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['追加したいカラム']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('minecraft:main')

    
class ImageUpload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="images/")
    userId = models.ForeignKey(LoginUser, on_delete=models.CASCADE)
    
    like = models.ManyToManyField(LoginUser, related_name='related_post', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title
    
# class FavoriteImg(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
#     userId = models.ForeignKey(LoginUser, on_delete=models.CASCADE)
#     imgId = models.ForeignKey(ImageUpload, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(default=timezone.now)
    
    
class ThreadUpload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=100)
    userId = models.ForeignKey(LoginUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)

    # def __str__(self):
    #     return self.title
    
class Thread(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    threadId = models.ForeignKey(ThreadUpload, on_delete=models.CASCADE, null=True)
    message = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(default=timezone.now)
    userId = models.ForeignKey(LoginUser, on_delete=models.CASCADE, null=True)
    # userName = models.CharField(max_length=64, null=True)
    
    
    class Meta:
        ordering = ('created_at',)
        
    # def __str__(self):
    #     return self.message
    
    
class ModUpload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    link = models.CharField(max_length=400)
    userId = models.ForeignKey(LoginUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.title
    
    
