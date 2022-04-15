from django.urls import path

from budget.main.views import HomeView, ContactsView, IncomesView, BudgetCreateView, BudgetEditView, \
    BudgetDeleteView, IncomeCreateView, IncomeEditView, IncomeDeleteView, ExpensesView, ExpenseCreateView, \
    ExpenseEditView, ExpenseDeleteView, BudgetsView, AllView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('budgets/', BudgetsView.as_view(), name='budgets'),
    path('budget-create/', BudgetCreateView.as_view(), name='budget create'),
    path('budget-edit/<int:pk>/', BudgetEditView.as_view(), name='budget edit'),
    path('budget-delete/<int:pk>/', BudgetDeleteView.as_view(), name='budget delete'),

    path('incomes/', IncomesView.as_view(), name='incomes'),
    path('income-create/', IncomeCreateView.as_view(), name='income create'),
    path('income-edit/<int:pk>/', IncomeEditView.as_view(), name='income edit'),
    path('income-delete/<int:pk>/', IncomeDeleteView.as_view(), name='income delete'),

    path('expenses/', ExpensesView.as_view(), name='expenses'),
    path('expense-create/', ExpenseCreateView.as_view(), name='expense create'),
    path('expense-edit/<int:pk>/', ExpenseEditView.as_view(), name='expense edit'),
    path('expense-delete/<int:pk>/', ExpenseDeleteView.as_view(), name='expense delete'),

    path('all/', AllView.as_view(), name='all'),
)
