from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Job  
from .serializers import JobSerializer  
import json
from jsons.models import Job



with open('/Users/yousefabdolmaleki/projects/json_api/api/linkedin_beautifulsoup/linkedin-jobs.json', encoding='utf-8') as data_file:
        json_data = json.loads(data_file.read())
        for job_data in json_data:
            jobs = Job.create(**job_data)
 



class JobView(APIView):
   
    def get(self, request, format=None):
        snippets = Job.objects.all()
        serializer = JobSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)