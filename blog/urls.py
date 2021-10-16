from django.urls import path
from .views import BlogDetailView, BlogListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('', BlogListView.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
