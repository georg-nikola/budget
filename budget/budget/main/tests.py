from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from budget.main.models import Budget, Income, Expense

UserModel = get_user_model()

VALID_USER_CREDENTIALS = {
    'username': 'testuser',
    'password': 'Asd123!.'
}


class BudgetsViewTests(django_test.TestCase):
    def test_when_user_is_logged_in__expect_can_open_budgets_page(self):
        UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
        self.client.login(**VALID_USER_CREDENTIALS)
        response = self.client.get(reverse('budgets'))
        self.assertTemplateUsed('main/budgets.html')

    def test_when_opening_budgets_and_not_logged_in__expect_302(self):
        response = self.client.get(reverse('budgets'))
        self.assertEqual(response.status_code, 302)


class IncomesViewTests(django_test.TestCase):
    def test_when_user_is_logged_in__expect_can_open_incomes_page(self):
        UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
        self.client.login(**VALID_USER_CREDENTIALS)
        response = self.client.get(reverse('incomes'))
        self.assertTemplateUsed('main/incomes.html')

    def test_when_opening_incomes_and_not_logged_in__expect_302(self):
        response = self.client.get(reverse('incomes'))
        self.assertEqual(response.status_code, 302)


class ExpensesViewTests(django_test.TestCase):
    def test_when_user_is_logged_in__expect_can_open_expenses_page(self):
        UserModel.objects.create_user(**VALID_USER_CREDENTIALS)
        self.client.login(**VALID_USER_CREDENTIALS)
        response = self.client.get(reverse('expenses'))
        self.assertTemplateUsed('main/expenses.html')

    def test_when_opening_expenses_and_not_logged_in__expect_302(self):
        response = self.client.get(reverse('expenses'))
        self.assertEqual(response.status_code, 302)
