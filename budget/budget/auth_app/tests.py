import logging
from datetime import date

from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from budget.auth_app.models import Profile
from budget.main.models import Budget, Income, Expense

UserModel = get_user_model()


class ProfileDetailsViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '12345qew',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
    }

    VALID_BUDGET_DATA = {
        'month': Budget.JANUARY,
        'value': 1,
    }

    VALID_EXPENSE_DATA = {
        'month': Budget.JANUARY,
        'value': 1,
    }

    VALID_INCOME_DATA = {
        'month': Budget.JANUARY,
        'value': 1,
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return (user, profile)

    def __create_budget_and_expense_and_income_for_user(self, user):
        budget = Budget.objects.create(
            **self.VALID_PET_DATA,
            user=user,
        )
        expense = Expense.objects.create(
            **self.VALID_PET_PHOTO_DATA,
            user=user,
        )
        income = Income.objects.create(
            **self.VALID_PET_PHOTO_DATA,
            user=user,
        )
        budget.save()
        expense.save()
        income.save()
        return budget, expense, income

    def __get_response_for_profile(self, profile):
        return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(reverse('profile details', kwargs={
            'pk': 1,
        }))

        self.assertEqual(404, response.status_code)

    def test_expect_correct_template(self):
        _, profile = self.__create_valid_user_and_profile()
        self.__get_response_for_profile(profile)
        self.assertTemplateUsed('auth_app/profile_details.html')

    def test_when_user_is_owner__expect_is_owner_to_be_true(self):
        _, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.__get_response_for_profile(profile)

        self.assertTrue(response.context['is_owner'])

    def test_when_user_is_not_owner__expect_is_owner_to_be_false(self):
        _, profile = self.__create_valid_user_and_profile()
        credentials = {
            'username': 'testuser2',
            'password': '12345qwe',
        }

        self.__create_user(**credentials)

        self.client.login(**credentials)

        response = self.__get_response_for_profile(profile)

        self.assertFalse(response.context['is_owner'])
