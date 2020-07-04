from django.db import models

# Create your models here.


class Todo(models.Model):
    data = models.CharField(max_length=200, default='')
    timeStamp = models.DateTimeField(blank=True)
    author = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name_plural = "todo"

    def __str__(self):
        return self.author
    
    