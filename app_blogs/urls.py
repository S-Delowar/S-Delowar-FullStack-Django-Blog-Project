from django.urls import path
from app_blogs import views

urlpatterns = [
    path('', views.blog_list_view, name='blog_list'),
    path('<uuid:blog_id>/', views.blog_detail_view, name='blog_detail'),
    path('create/', views.blog_create_view, name="blog_create"),
    path('<uuid:blog_id>/edit/', views.blog_edit_view, name="blog_edit"),
    path('<uuid:blog_id>/delete/', views.blog_delete_view, name="blog_delete"),
    path('search-results', views.search_results_view, name='search_results'),
]
