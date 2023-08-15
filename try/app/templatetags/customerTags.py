from django import template

register = template.Library()


@register.simple_tag()
def salutation(value):
    return f"{value}"