from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField(default='')

    def __str__(self):
        return self.question


class Qs(models.Model):
    qs = models.CharField(max_length=1000)

    def __str__(self):
        return self.qs

def json(self):
    return {
        'question': self.qs,
        'answer': self.answer,
    }  