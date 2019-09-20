
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('favorites', views.FavoriteViewSet, basename='favorites')

urlpatterns = [
        path('auditlog/', views.AuditlogListAPIView.as_view(), name='auditlog'),
        path('categories/', views.CategoryListAPIView.as_view(), name='categories'),
    ]

urlpatterns += router.urls
