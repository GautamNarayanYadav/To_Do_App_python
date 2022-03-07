from datetime import timezone
from django.db import models
import datetime
# Create your models here.
class NewTask(models.Model):
    AddTask=models.CharField(max_length=30)
    time=models.TimeField(auto_now=False, auto_now_add=False)