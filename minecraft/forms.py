from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from .models import ImageUpload
from .models import ThreadUpload
from .models import ModUpload
from .models import LoginUser
from .models import Thread

class CreateAccountForm(forms.ModelForm):
    username = forms.CharField(label='name')
    email = forms.EmailField(label='email address')
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='password(再入力)', widget=forms.PasswordInput())
    class Meta:
        model = LoginUser
        fields = ["username", "email", "password","password2"]

    
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('password2')
        if password != confirm_password:
            raise forms.ValidationError('パスワードが一致しません')
        else:
            user = super().save(commit=False)
            validate_password(self.cleaned_data['password'], user)
    
    
class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email Address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    remember = forms.BooleanField(label='keep login', required=False)


class ImageUploadForm(forms.ModelForm):
    # file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = ImageUpload
        fields = ("title","img",)
        exclude = ["userId"]
        
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        
    def save(self, commit=True):
        user_obj = super().save(commit=False)
        if self.user:
            user_obj.userId = self.user
        if commit:
            user_obj.save()
        return user_obj
    
class ThreadUploadForm(forms.ModelForm):
    
    class Meta:
        model = ThreadUpload
        fields = ("title",)
        exclude = ["userId"]
        
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        
    def save(self, commit=True):
        user_obj = super().save(commit=False)
        if self.user:
            user_obj.userId = self.user
        if commit:
            user_obj.save()
        return user_obj
    
class ThreadPostForm(forms.ModelForm):
    
    class Meta:
        model = Thread
        fields = ("message",)
        exclude = ["threadId","userId",]



class ModUploadForm(forms.ModelForm):
    
    class Meta:
        model = ModUpload
        fields = ("title","text","link")
        exclude = ["userId"]
        
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        
    def save(self, commit=True):
        user_obj = super().save(commit=False)
        if self.user:
            user_obj.userId = self.user
        if commit:
            user_obj.save()
        return user_obj