from django.db import models

# Create your models here.
class KodPocztowy(models.Model):
	kp = models.CharField(max_length=6)
		