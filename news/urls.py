from django.urls import path

import news.views as views

urlpatterns = [
    path('news-create/', views.NewsCreateAPIView.as_view()),
    path('news-list/', views.NewsListAPIView.as_view()),
    path('news-detail/<int:pk>/', views.NewsRetrieveAPIView.as_view()),
    path('news-update/<int:pk>/', views.NewsUpdateAPIView.as_view()),
    path('news-delete/<int:pk>/', views.NewsDeleteAPIView.as_view()),
    path('category-create/', views.CategoryCreateAPIView.as_view()),
    path('category-list/', views.CategoryListAPIView.as_view()),
    path('category-detail/<int:pk>/', views.CategoryRetrieveAPIView.as_view()),
    path('category-update/<int:pk>/', views.CategoryUpdateAPIView.as_view()),
    path('category-delete/<int:pk>/', views.CategoryDeleteAPIView.as_view()),
]