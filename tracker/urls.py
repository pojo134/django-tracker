from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.medicine_log, name='medicine_log'),
    path('mark_taken/<int:log_id>/', views.mark_taken, name='mark_taken'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('deactivate_medicine/<int:medicine_id>/', views.deactivate_medicine, name='deactivate_medicine'),
]
