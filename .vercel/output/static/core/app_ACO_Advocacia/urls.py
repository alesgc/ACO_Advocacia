from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name="index"),
    path('agency/', views.agency ,name="agency"),
    path('solutions/', views.solutions ,name="solutions"),
    path('politics/', views.politics ,name="politics"),
    path('contact/', views.contact ,name="contact"),
    path('layoutp/', views.layoutp ,name="layoutp"),
]
