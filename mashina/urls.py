from django.urls import path
from .views import CarListAPIView, DetailCarAPIView, CreateImageAPIView


urlpatterns = [
    path('cars/', CarListAPIView.as_view()),
    path('cars/<str:number>/', DetailCarAPIView.as_view()),
    path('images/', CreateImageAPIView.as_view()),
]