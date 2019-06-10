from django.db import models
class RegistrationData(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    user_name=models.CharField(max_length=30)
    password1=models.CharField(max_length=20)
    password2=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    number=models.BigIntegerField()
