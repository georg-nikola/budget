from django import test as django_test
from django.core.exceptions import ValidationError

from budget.common.validators import validate_only_letters


class ValidateOnlyLettersTests(django_test.TestCase):

    def test_when_not_only_letters(self):
        with self.assertRaises(ValidationError):
            validate_only_letters('123')
