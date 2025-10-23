from django.urls import path
from .views import MainPageView, DetailPageView, AddPostView, EditPostView, DeletePostView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('/detail/<str:slug>/', DetailPageView.as_view(), name='detail'),
    path('add-post/', AddPostView.as_view(), name='add'),
    path('edit/<str:slug>/', EditPostView.as_view(), name='edit'),
    path('delete/<str:slug>', DeletePostView.as_view(), name='del'),
]

