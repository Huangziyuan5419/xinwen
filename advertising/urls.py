from django.urls import path

from . import views

urlpatterns = [
    path('slides/', views.AdvertisingView.as_view())
]