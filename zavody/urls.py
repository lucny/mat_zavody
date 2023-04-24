from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kluby/', views.KlubListView.as_view(), name='seznam_klubu'),
    path('kluby/<int:pk>', views.KlubDetailView.as_view(), name='detail_klubu'),
]