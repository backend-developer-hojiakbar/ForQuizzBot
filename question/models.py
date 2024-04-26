from django.db import models

# Create your models here.
class Answer(models.Model):
    text = models.CharField(max_length=33)

    def __str__(self):
        return self.text
