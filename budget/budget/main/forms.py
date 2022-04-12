from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from budget.common.helpers import BootstrapFormMixin, DisableFieldsFormMixin
from budget.main.models import Budget, Income, Expense


class CreateBudgetForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        budget = super().save(commit=False)

        budget.user = self.user
        if commit:
            budget.save()

        return budget

    class Meta:
        model = Budget
        fields = ('month', 'value')


class CreateIncomeForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        income = super().save(commit=False)

        income.user = self.user
        if commit:
            income.save()

        return income

    class Meta:
        model = Income
        fields = ('month', 'value')


class CreateExpenseForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        expense = super().save(commit=False)

        expense.user = self.user
        if commit:
            expense.save()

        return expense

    class Meta:
        model = Expense
        fields = ('month', 'value')
