from django.db import models

class Advice(models.Model):
    letter = models.CharField(max_length=4)
    text = models.TextField()

    def __str__(self):
        return self.letter
