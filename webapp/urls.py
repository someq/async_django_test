from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('async_view/', views.async_view, name='async_view'),
    path('async_cbv/', views.AsyncCbv.as_view(), name='async_cbv')
]
