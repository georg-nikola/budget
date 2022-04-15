from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from budget.main.models import Budget, Income, Expense

UserModel = get_user_model()

VALID_USER_CREDENTIALS = {
    'username': 'testuser',
    'password': 'Asd123!.'
}


class BudgetViewsTests(django_test.TestCase):
    VALID_BUDGET = {
        'month': 'January',
        'value': 10,
    }

    def test_when_user_is_logged_in__expect_can_open_budgets_page(self):
        UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
        self.client.login(**VALID_USER_CREDENTIALS)
        response = self.client.get(reverse('budgets'))
        self.assertTemplateUsed('main/budgets.html')

    def test_when_opening_budgets_and_not_logged_in__expect_302(self):
        response = self.client.get(reverse('budgets'))
        self.assertEqual(response.status_code, 302)

    def test_when_user_is_logged_in__expect_can_open_budget_create_page(self):
        UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
        self.client.login(**VALID_USER_CREDENTIALS)
        response = self.client.get(reverse('budget create'))
        self.assertTemplateUsed('main/budget_create.html')

    def test_when_user_is_logged_in__expect_can_create_budget_and_owner_is_true(self):
        user = UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
        self.client.login(**VALID_USER_CREDENTIALS)
        expense = Expense.objects.create(**self.VALID_BUDGET, user=user)
        response = self.client.get(reverse('expense edit', kwargs={'pk': expense.pk}))
        self.assertTrue(response.context['is_owner'])


class IncomeViewsTests(django_test.TestCase):
    VALID_INCOME = {
        'month': 'January',
        'value': 10,
    }

    def test_when_user_is_logged_in__expect_can_open_incomes_page(self):
        UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
        self.client.login(**VALID_USER_CREDENTIALS)
        response = self.client.get(reverse('incomes'))
        self.assertTemplateUsed('main/incomes.html')

    def test_when_opening_incomes_and_not_logged_in__expect_302(self):
        response = self.client.get(reverse('incomes'))
        self.assertEqual(response.status_code, 302)

    def test_when_user_is_logged_in__expect_can_open_income_create_page(self):
        UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
        self.client.login(**VALID_USER_CREDENTIALS)
        response = self.client.get(reverse('income create'))
        self.assertTemplateUsed('main/income_create.html')

    def test_when_user_is_logged_in__expect_can_create_income_and_owner_is_true(self):
        user = UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
        self.client.login(**VALID_USER_CREDENTIALS)
        expense = Expense.objects.create(**self.VALID_INCOME, user=user)
        response = self.client.get(reverse('expense edit', kwargs={'pk': expense.pk}))
        self.assertTrue(response.context['is_owner'])


class ExpenseViewsTests(django_test.TestCase):
    VALID_EXPENSE = {
        'month': 'January',
        'value': 10,
    }

    def test_when_user_is_logged_in__expect_can_open_expenses_page(self):
        UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
        self.client.login(**VALID_USER_CREDENTIALS)
        response = self.client.get(reverse('expenses'))
        self.assertTemplateUsed('main/expenses.html')

    def test_when_opening_expenses_and_not_logged_in__expect_302(self):
        response = self.client.get(reverse('expenses'))
        self.assertEqual(response.status_code, 302)

    def test_when_user_is_logged_in__expect_can_open_expense_create_page(self):
        UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
        self.client.login(**VALID_USER_CREDENTIALS)
        response = self.client.get(reverse('income create'))
        self.assertTemplateUsed('main/income_create.html')

    def test_when_user_is_logged_in__expect_can_create_expense_and_owner_is_true(self):
        user = UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
        self.client.login(**VALID_USER_CREDENTIALS)
        expense = Expense.objects.create(**self.VALID_EXPENSE, user=user)
        response = self.client.get(reverse('expense edit', kwargs={'pk': expense.pk}))
        self.assertTrue(response.context['is_owner'])
