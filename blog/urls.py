from django.urls import path
from .views import MainPageView, DetailPageView, AddPostView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('/detail/<str:slug>/', DetailPageView.as_view(), name='detail'),
    path('add-post/', AddPostView.as_view(), name='add'),
]

