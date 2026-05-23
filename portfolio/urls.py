from django.urls import path
from .views import IndexView, ProjectDetailView, ServiceDetailView, ContactProcessView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('service/', ServiceDetailView.as_view(), name='service_details'),
    path('contact/', ContactProcessView.as_view(), name='contact'),
]
