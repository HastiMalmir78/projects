from .views import JobView  
from django.urls import path  

urlpatterns = [  
    path('job/', JobView.as_view())  
]  