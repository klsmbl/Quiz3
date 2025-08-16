from django.db import models
from django.conf import settings
from django.utils import timezone


class JobOpening(models.Model):
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    min_offer = models.DecimalField(max_digits=10, decimal_places=2)
    max_offer = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title


class JobApplicant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(JobOpening, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(default=timezone.now)
    resume = models.FileField(upload_to='resumes/')


    class Meta:
        unique_together = ('user', 'job')

    def __str__(self):
        return f"{self.user.username} applied for {self.job.job_title}"