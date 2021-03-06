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
    path('user/history/', views.HistoryView.as_view(), name='history_view'),
    path('faq/', views.FAQView.as_view(), name='faq_view'),
    path('about-us/', views.FAQView.as_view(), name='contact_view'),
    path('contact-us/', views.ContactView.as_view(), name='contact_view'),
    path('user/profile/', views.ProfileView.as_view(), name='profile_view'),
    path('user/wallet/', views.WalletView.as_view(), name='wallet_view'),
    path('user/upload-id/', views.UploadIDView.as_view(), name='upload_id_view'),


]
