from django.urls import path

from .views import *



urlpatterns = [
    path("", index, name="index"),
    path('update/<int:pk>/',update, name="update"),
    path('delete/<int:pk>/',delete, name="delete"),
    path('finish/<int:pk>/',finishtodo, name="finish"),
    path('continue/<int:pk>/',davometish, name="davom")

]