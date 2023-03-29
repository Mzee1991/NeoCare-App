
from django import template
register = template.Library()

@register.filter(name='attr')
def attr(field, value):
    return field.as_widget(attrs={'style': value})
