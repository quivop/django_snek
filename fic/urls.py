from django.urls import path

# mah first url~

from . import views

urlpatterns = [
	path('', views.index, name='index'),
]