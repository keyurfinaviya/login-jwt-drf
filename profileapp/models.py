from django.db import models
from application.models import User

# Create your models here.

class UserProfile(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	first_name = models.CharField(max_length=50, unique=False)
	last_name = models.CharField(max_length=50, unique=False)
	phone_number = models.CharField(max_length=10, unique=True, null=False, blank=False)
	age = models.PositiveIntegerField(null=False, blank=False)

	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
		)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

	class Meta:
	    '''
	    to set table name in database
	    '''
	    db_table = "profile"