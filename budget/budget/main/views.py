from django.shortcuts import render
from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class ContactsView(views.TemplateView):
    template_name = 'main/contacts.html'
