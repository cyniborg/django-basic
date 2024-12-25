from django.urls import path
from app import views
urlpatterns = [
    path('', views.helloWorld, name = 'home_page'),
    path('job/<int:id>', views.jobDetail, name = "job_detail"),
    path ('template/', views.helloTemplate)
]