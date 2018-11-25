from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('signup/', views.signup, name='signup'),

	path('profile/<int:user_id>/', views.user_info, name='user_info'),
	path('formuserpage/', views.form_user_view, name='formuserpage'),
	path('profile/<int:user_id>/tweet/', views.form_user_id_view, name='fromuserpageid'),
]
