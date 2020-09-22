from django.db import models
from django.shortcuts import reverse

class Job(models.Model):

    
    title = models.CharField(max_length=100)
    start_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    end_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    
    

    class Meta:
        verbose_name = ("Job")
        verbose_name_plural = ("Jobs")

    def get_absolute_url(self):
        return reverse("job_details", kwargs={"pk": self.pk})