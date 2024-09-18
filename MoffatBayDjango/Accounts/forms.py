from django import forms
from .models import CustomUser
from django.contrib.auth.hashers import make_password, check_password
import uuid

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',  # Bootstrap class for styling
            'minlength': '8',
            'placeholder': 'Password'
        }),
        min_length=8
    )
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        min_length = 8;
        # Add your custom password validation logic here
        if (password) < min_length:
            raise forms.ValidationError('Password must be at least {min_length} characters long')
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('Password must contain at least one digit.')
        if not any(char.isupper() for char in password):
            raise forms.ValidationError('Password must contain at least one uppercase character.')
        if not any(char.islower() for char in password):
            raise forms.ValidationError('Password must contain at least one lowercase character.')
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password_salt = uuid.uuid4().hex  # Generate a unique salt
        user.password_hash = make_password(self.cleaned_data['password'], salt=user.password_salt)
        if commit:
            user.save()
        return user
    

class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'required': 'required'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': 'required'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        try:
            user = CustomUser.objects.get(email=email)
            hashed_password = make_password(password, salt=user.password_salt)
            if hashed_password == user.password_hash:
                cleaned_data['user'] = user
                cleaned_data['password'] = hashed_password
                return cleaned_data
            else:
                raise forms.ValidationError('Invalid password.' + hashed_password + ' ' + user.password_hash)
        except CustomUser.DoesNotExist:
            raise forms.ValidationError('Invalid email.')
        
