from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from budget.main.forms import CreateBudgetForm, CreateIncomeForm, CreateExpenseForm
from budget.main.models import Budget, Income, Expense


class HomeView(views.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class ContactsView(views.TemplateView):
    template_name = 'main/contacts.html'


class BudgetsView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Budget
    template_name = 'main/budgets.html'
    context_object_name = 'budgets'


class BudgetCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Budget
    form_class = CreateBudgetForm
    template_name = 'main/budget_create.html'
    success_url = reverse_lazy('budgets')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['is_owner'] = self.object.user == self.request.user
    #     return context


class BudgetEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Budget
    fields = ('month', 'value',)
    template_name = 'main/budget_edit.html'

    success_url = reverse_lazy('budgets')


class BudgetDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Budget
    template_name = 'main/budget_confirm_delete.html'
    success_url = reverse_lazy('budgets')


class IncomesView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Income
    template_name = 'main/incomes.html'
    context_object_name = 'incomes'


class IncomeCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Income
    template_name = 'main/income_create.html'
    form_class = CreateIncomeForm
    success_url = reverse_lazy('incomes')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class IncomeEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Income
    template_name = 'main/income_edit.html'
    fields = ('month', 'value',)
    success_url = reverse_lazy('incomes')


class IncomeDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Income
    template_name = 'main/income_confirm_delete.html'
    success_url = reverse_lazy('incomes')


class ExpensesView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Expense
    template_name = 'main/expenses.html'
    context_object_name = 'expenses'


class ExpenseCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Expense
    template_name = 'main/expense_create.html'
    success_url = reverse_lazy('expenses')
    form_class = CreateExpenseForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ExpenseEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Expense
    template_name = 'main/expense_edit.html'
    fields = ('month', 'value',)
    success_url = reverse_lazy('expenses')


class ExpenseDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Expense
    template_name = 'main/expense_delete.html'
    success_url = reverse_lazy('expenses')
