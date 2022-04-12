from django.urls import path

from budget.main.views import HomeView, ContactsView, IncomesView, BudgetCreateView, BudgetEditView, \
    BudgetDeleteView, IncomeDetailsView, IncomeCreateView, IncomeEditView, IncomeDeleteView, ExpensesView, \
    ExpenseDetailsView, ExpenseCreateView, ExpenseEditView, ExpenseDeleteView, BudgetDetailsView, BudgetsView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('budgets/', BudgetsView.as_view(), name='budgets'),
    path('budgets/', BudgetDetailsView.as_view(), name='budget details'),
    path('budget-create/', BudgetCreateView.as_view(), name='budget create'),
    path('budget-edit/', BudgetEditView.as_view(), name='budget edit'),
    path('budget-delete/', BudgetDeleteView.as_view(), name='budget delete'),

    path('incomes/', IncomesView.as_view(), name='incomes'),
    path('income-details/', IncomeDetailsView.as_view(), name='income details'),
    path('income-create/', IncomeCreateView.as_view(), name='income create'),
    path('income-edit/', IncomeEditView.as_view(), name='income edit'),
    path('income-delete/', IncomeDeleteView.as_view(), name='income delete'),

    path('expenses/', ExpensesView.as_view(), name='expenses'),
    path('expense-details/', ExpenseDetailsView.as_view(), name='expense details'),
    path('expense-create/', ExpenseCreateView.as_view(), name='expense create'),
    path('expense-edit/', ExpenseEditView.as_view(), name='expense edit'),
    path('expense-delete/', ExpenseDeleteView.as_view(), name='expense create'),
)
