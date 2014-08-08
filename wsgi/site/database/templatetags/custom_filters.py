from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

speeds = {
    'F': 'Fast',
    'S': 'Slow',
    'FS': 'Fast/Slow'
}

@register.filter
@stringfilter
def convert_speed(speed):
    return speeds[speed]

@register.filter
@stringfilter
def hyphenate(string):
    return string.replace(" ", "-")