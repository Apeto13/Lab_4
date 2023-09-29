from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("taxRate", views.taxRate, name="taxRate"),
    path("<str:number>", views.anyNumber, name="anyNumber"),
]
