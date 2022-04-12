from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

UserModel = get_user_model()


class Income(models.Model):
    NAME_MAX_LENGTH = 30
    VALUE_MIN = 0
    JANUARY = 'January'
    FEBRUARY = 'February'
    MARCH = 'March'
    APRIL = 'April'
    MAY = 'May'
    JUNE = 'June'
    JULY = 'July'
    AUGUST = 'August'
    SEPTEMBER = 'September'
    OCTOBER = 'October'
    NOVEMBER = 'November'
    DECEMBER = 'December'

    MONTHS = [(x, x) for x in
              (JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER)]
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    month = models.CharField(
        max_length=max(len(x) for x, _ in MONTHS),
        choices=MONTHS,
        default='January'
    )

    value = models.FloatField(
        validators=[MinValueValidator(VALUE_MIN)],
        default=0
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Budget(models.Model):
    VALUE_MIN = 0
    JANUARY = 'January'
    FEBRUARY = 'February'
    MARCH = 'March'
    APRIL = 'April'
    MAY = 'May'
    JUNE = 'June'
    JULY = 'July'
    AUGUST = 'August'
    SEPTEMBER = 'September'
    OCTOBER = 'October'
    NOVEMBER = 'November'
    DECEMBER = 'December'

    MONTHS = [(x, x) for x in
              (JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER)]

    month = models.CharField(
        max_length=max(len(x) for x, _ in MONTHS),
        choices=MONTHS,
        default='January'

    )

    value = models.FloatField(
        validators=[MinValueValidator(VALUE_MIN)],
        default=0
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Expense(models.Model):
    NAME_MAX_LENGTH = 30
    VALUE_MIN = 0
    JANUARY = 'January'
    FEBRUARY = 'February'
    MARCH = 'March'
    APRIL = 'April'
    MAY = 'May'
    JUNE = 'June'
    JULY = 'July'
    AUGUST = 'August'
    SEPTEMBER = 'September'
    OCTOBER = 'October'
    NOVEMBER = 'November'
    DECEMBER = 'December'

    MONTHS = [(x, x) for x in
              (JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    value = models.FloatField(
        validators=[MinValueValidator(VALUE_MIN)],
        default=0
    )

    month = models.CharField(
        max_length=max(len(x) for x, _ in MONTHS),
        choices=MONTHS,
        default='January'
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
