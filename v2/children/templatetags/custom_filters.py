from django import template
from datetime import date

register = template.Library()

@register.filter
def calculate_age(date_of_birth):
    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

    years = age
    months = today.month - date_of_birth.month
    if today.day < date_of_birth.day:
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    return f"{years} years, {months} months"
