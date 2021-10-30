from django.db import models

# Create your models here.


class Advisor(models.Model):
    Advisor_name = models.CharField(max_length=50)
    advisor_img_url  = models.URLField(max_length=5000)
    def __str__(self):
        return self.Advisor_name

