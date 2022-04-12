from django.contrib import admin

from budget.main.models import Budget, Income, Expense


class BudgetInlineAdmin(admin.StackedInline):
    model = Budget


class IncomeInlineAdmin(admin.StackedInline):
    model = Budget


class ExpenseInlineAdmin(admin.StackedInline):
    model = Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('month', 'value', 'user')


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('month', 'value', 'user')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('month', 'value', 'user')
