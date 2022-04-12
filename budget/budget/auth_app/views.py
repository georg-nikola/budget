from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from budget.auth_app.forms import CreateProfileForm
from budget.auth_app.models import Profile


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


class ProfileDetailView(views.DetailView, auth_mixins.LoginRequiredMixin):
    model = Profile
    template_name = 'auth_app/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is a Profile
        context.update({
            'is_owner': self.object.user_id == self.request.user.id,
        })

        return context


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'auth_app/change_password.html'


class EditProfileView(auth_views.FormView):
    pass


class DeleteProfileView(auth_views.FormView):
    pass
