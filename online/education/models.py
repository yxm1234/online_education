from django.db import models

# Create your models here.


class Test(models.Model):
    title = models.CharField(max_length=20, null=True)
    introduction = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.title
