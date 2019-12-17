from django.urls import path
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from .views import IndexView
from django.urls import path

urlpatterns = [
	url(r'^$',IndexView.as_view(),name="home"),
    path('post/', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('admit/', views.admit, name='admit'),	
	path('admit/<int:pk>/', views.admit_detail, name='admit_detail'),
    path('answer/', views.answer, name='answer'),	
	path('answer/<int:pk>/', views.answer_detail, name='answer_detail'),
    path('admission/', views.admission, name='admission'),	
	path('admission/<int:pk>/', views.admission_detail, name='admission_detail'),
    path('result/', views.result, name='result'),	
	path('result/<int:pk>/', views.result_detail, name='result_detail'),
    path('important/', views.important, name='important'),	
	path('important/<int:pk>/', views.important_detail, name='important_detail'),	
]