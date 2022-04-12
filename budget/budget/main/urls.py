from django.urls import path

from budget.main.views import HomeView, ContactsView, BudgetView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('budget/', BudgetView.as_view(), name='budget'),
    path('budget-create/', BudgetView.as_view(), name='budget'),
    path('budget-edit/', BudgetView.as_view(), name='budget'),
    path('budget-delete/', BudgetView.as_view(), name='budget'),
)
