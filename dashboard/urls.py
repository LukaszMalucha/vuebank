from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    ]