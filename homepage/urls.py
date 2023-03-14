from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('inner-page/', views.inner_page, name='inner_page'),
]