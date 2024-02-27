from django.db import models
from django.urls import reverse
# Create your models here.

class Projects(models.Model):
    id_projects=models.AutoField
    project_name=models.CharField(max_length=101)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    about=models.TextField()
    date_manufactured=models.DateField()
    
    def __str__(self):
        return self.project_name
    
    def get_absolute_url(self):
        return reverse("datail", args=[str(self.pk)])

