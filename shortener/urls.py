from django.urls import path
from . import views

app_name = "shortener"

urlpatterns = [
    path('', views.shortener, name="shortener"),
    path('<slug:slug>', views.shortener, name="result"),
    path('redirect/<slug:slug>', views.redirect_view, name="redirect"),
]