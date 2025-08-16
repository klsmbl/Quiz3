from django.urls import path
from . import views
from .views import JobUpdateView, JobDeleteView

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/<int:pk>/apply/', views.apply_for_job, name='apply_for_job'),
    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
]