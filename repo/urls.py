from django.urls import path

from . import views

urlpatterns = [
    path('', views.SnippetList.as_view(), name='home'),
    path('snippet/<slug:slug>/', views.SnippetDetail.as_view(), name='post_detail'),
]
