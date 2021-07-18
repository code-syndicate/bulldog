from django.urls import path

from . import views

app_name = 'services'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_view'),
    path('authenticate-user/', views.AuthView.as_view(), name='auth_view'),
    path('user/new/', views.CreateUserView.as_view(), name='create_view'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard_view'),
    path('user/verify/', views.VerifyCodeView.as_view(), name='verify_view'),
    path('user/logout/', views.LogoutView.as_view(), name='logout_view'),
    path('user/verify-deposit/', views.VerifyDepositView.as_view(),
         name='verify_deposit_view'),
    path('user/withdraw/', views.WithdrawView.as_view(), name='withdraw_view'),
    path('user/history/', views.HistoryView.as_view(), name='history_view')

]
