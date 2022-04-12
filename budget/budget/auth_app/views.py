from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from budget.auth_app.forms import CreateProfileForm


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'auth_app/profile_create.html'
    success_url = reverse_lazy('index')


class UserLoginView(auth_views.LoginView):
    template_name = 'auth_app/login_page.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()
