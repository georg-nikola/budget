from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from budget.auth_app.models import Profile

UserModel = get_user_model()


class ProfileDetailsViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': 'Asd123!.'
    }

    VALID_PROFILE_DATA = {
        'first_name': 'test',
        'last_name': 'test',
        'email': 'test@test.com'
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user
        )
        return user, profile

    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(reverse('profile details', kwargs={
            'pk': 1,
        }))
        self.assertEqual(response.status_code, 404)

    def test_when_all_valid__expect_correct_template(self):
        user, profile = self.__create_valid_user_and_profile()
        response = self.client.get(reverse('profile details', kwargs={
            'pk': profile.pk,
        }))
        self.assertTemplateUsed('auth_app/profile_details.html')

    def test_when_user_is_owner__expect_is_owner_to_be_true(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)
        response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        self.assertTrue(response.context['is_owner'])

    def test_when_user_is_not_owner__expect_is_owner_to_be_false(self):
        _, profile = self.__create_valid_user_and_profile()
        credentials = {
            'username': 'testuser2',
            'password': 'Asd123!.',
        }

        self.__create_user(**credentials)
        self.client.login(**credentials)
        response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        self.assertFalse(response.context['is_owner'])
