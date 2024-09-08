from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid

class CustomUser(AbstractUser):
    userID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, db_column='FirstName')
    last_name = models.CharField(max_length=50, db_column='LastName')
    email = models.EmailField(unique=True, db_column='Email')
    phone = models.CharField(max_length=15, db_column='PhoneNumber', blank=True, null=True)
    password_hash = models.CharField(max_length=128, db_column='PasswordHash', blank=True, null=True)
    password_salt = models.CharField(max_length=128, db_column='Salt', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, db_column='CreatedAt')
    last_login = models.DateTimeField(default=timezone.now, db_column='lastLogin')
    # fields I am excluding from the user model
    is_superuser = None
    is_staff = None
    is_active = None
    date_joined = None
    username = None
    password = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'password_hash', 'password_salt']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups'  # Unique reverse accessor name
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions'  # Unique reverse accessor name
    )

    class Meta:
        db_table = 'user'

    def save(self, *args, **kwargs):
        self.username = self.email
        super(CustomUser, self).save(*args, **kwargs)

# Create session model
class Session(models.Model):
    sessionID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='UserID')
    sessionToken = models.UUIDField(default=uuid.uuid4, db_column='SessionToken')
    created_date = models.DateTimeField(default=timezone.now, db_column='CreatedAt')
    expires_date = models.DateTimeField(db_column='ExpiresAt')

    class Meta:
        db_table = 'session'