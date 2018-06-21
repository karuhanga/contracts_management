from django import template

register = template.Library()


@register.filter
def in_list(value, the_list):
    value = str(value)
    return value in the_list.split(',')
