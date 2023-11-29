from django.urls import path

from accounts.views import RegisterView, LoginView
from accounts.views.user_login_view import logout_view

from accounts.views.user_profile_view import UserDetailView

from accounts.views.user_department_view import DepartmentView

from accounts.views.user_password_change_view import UserPasswordChangeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/password_change', UserPasswordChangeView.as_view(), name='password_change'),
    path('profile/<int:pk>', UserDetailView.as_view(), name='profile'),

    path('add_department/', DepartmentView.as_view(), name='add_department'),
]
