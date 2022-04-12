from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class ContactsView(views.TemplateView):
    template_name = 'main/contacts.html'


class BudgetsView(views.ListView):
    template_name = 'main/budget.html'


class BudgetDetailsView(views.TemplateView):
    template_name = 'main/budget.html'


class BudgetCreateView(views.CreateView):
    template_name = 'main/budget-create.html'
    success_url = reverse_lazy('budget')


class BudgetEditView(views.UpdateView):
    template_name = 'main/budget-edit.html'
    success_url = reverse_lazy('budget')


class BudgetDeleteView(views.DeleteView):
    template_name = 'main/budget-delete.html'
    success_url = reverse_lazy('budget')


class IncomesView(views.ListView):
    template_name = 'main/incomes.html'


class IncomeDetailsView(views.TemplateView):
    template_name = 'main/income-details.html'


class IncomeCreateView(views.CreateView):
    template_name = 'main/income-create.html'


class IncomeEditView(views.TemplateView):
    template_name = 'main/income-edit.html'


class IncomeDeleteView(views.TemplateView):
    template_name = 'main/income-delete.html'


class ExpensesView(views.ListView):
    template_name = 'main/expenses.html'


class ExpenseDetailsView(views.TemplateView):
    template_name = 'main/expense-details.html'


class ExpenseCreateView(views.CreateView):
    template_name = 'main/expense-create.html'


class ExpenseEditView(views.UpdateView):
    template_name = 'main/expense-edit.html'


class ExpenseDeleteView(views.DetailView):
    template_name = 'main/expense-delete.html'
