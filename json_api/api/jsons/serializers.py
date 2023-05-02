from rest_framework import serializers
from jsons.models import Job


class JobSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(max_length=255)
    job_url = serializers.CharField(max_length=255)
    company_name = serializers.CharField(max_length=255)
    company_link = serializers.CharField(max_length=255)
    company_location = serializers.CharField(max_length=150)


    class Meta:
        model = Job
        fields = ('__all__')