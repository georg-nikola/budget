from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from budget.auth_app.views import UserLoginView, UserRegisterView, ChangeUserPasswordView, ProfileDetailView, \
    EditProfileView, DeleteProfileView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('change-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('index')), name='password_change_done'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile details'),
    path('edit/', EditProfileView.as_view(), name='edit profile'),
    path('delete/', DeleteProfileView.as_view(), name='delete profile'),

)
