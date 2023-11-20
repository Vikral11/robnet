from django.db import models

# Create your models here.



class Form1(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name + " " + self.phone
    


class FormTwo(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=15, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    file = models.FileField(upload_to ='uploads/')


        # def __str__(self) -> str:
        #     return self.name + " " + self.designation