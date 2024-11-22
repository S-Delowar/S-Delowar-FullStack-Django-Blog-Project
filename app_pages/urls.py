from django.urls import path
from app_pages import views

urlpatterns = [
    path('', views.home_page_view, name='home' ),
]
