from django.db import models



class Job(models.Model):
    job_title = models.CharField(max_length=255)
    job_url = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_link = models.CharField(max_length=255)
    company_location = models.CharField(max_length=150)


    @classmethod
    def create(cls, **kwargs):
        job = cls.objects.create(
            job_title=kwargs['job_title'],
            company_name=kwargs['company_name'],
            company_location =kwargs['company_location'],
            job_url=kwargs['job_url']
        )
        return job

