from django.urls import path
from .import views


app_name = 'services'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_view'),
    path('authenticate-user/', views.AuthView.as_view(), name='auth_view'),
    path('user/new/', views.CreateUserView.as_view(), name='create_view'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard_view'),
    path('user/verify/', views.VerifyCodeView.as_view(), name='verify_view'),

]
