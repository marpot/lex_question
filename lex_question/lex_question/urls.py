from django.contrib import admin
from django.urls import path, include
from question import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('question', include('question.urls')),
    path('registration/', views.registration_view, name='registration'),
]
