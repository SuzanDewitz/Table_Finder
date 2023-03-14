from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inner-page/', views.inner_page, name='inner_page'),
    path('accounts/', include('allauth.urls')),
]
