from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from budget.auth_app.views import UserLoginView, UserRegisterView, ChangeUserPasswordView, ProfileDetailView, \
    EditProfileView, DeleteProfileView, UserLogoutView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),

    path('change-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('index')), name='password_change_done'),

    path('<int:pk>/', ProfileDetailView.as_view(), name='profile details'),
    path('edit/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('delete/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),

)
