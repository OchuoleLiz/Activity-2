from django.urls import path
from .views import BlogDetailView, BlogListView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('', BlogListView.as_view(), name='home'),
]

handler404 = 'blog.views.entry_not_found'