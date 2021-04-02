from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):

	def create_user(self, email, password=None):

		if not email:
			raise ValueError('Users Must Have an Email Address')

		user = self.model(
			email=self.normalize_email(email)
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		if password is None:
			raise TypeError('Superuser must have a password')

		user = self.create_user(email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()

		return user


class User(AbstractBaseUser, PermissionsMixin):

	id = models.AutoField(primary_key=True)
	email = models.EmailField(
		verbose_name='email_address',
		max_length=255,
		unique=True
		)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELD = []

	objects = UserManager()

	def __str__(self):
		return self.email

