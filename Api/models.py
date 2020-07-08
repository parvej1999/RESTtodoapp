from django.db import models

# Create your models here.
class task(models.Model):
    title = models.CharField(max_length = 400)
    description = models.TextField()
    scheduled_date = models.DateField(auto_now_add=True)
    scheduled_time = models.TimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title