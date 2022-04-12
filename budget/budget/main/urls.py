from django.urls import path

from budget.main.views import HomeView, ContactsView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
)
