from django.db import models

class Job(models.Model):

    
    training_title = models.CharField(max_length=100)
    start_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    end_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    max_capacity = models.IntegerField()
    

    class Meta:
        verbose_name = ("Job")
        verbose_name_plural = ("Jobs")