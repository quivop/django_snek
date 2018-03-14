from django.urls import path

from . import views

# mah first url~

urlpatterns = [
	# ex: /fic/
	path('', views.index, name='index'),
	# ex: /fic/5/
	path('<int:fanfic_id>/', views.detail, name='detail')
]
