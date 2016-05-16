from django import template

import os

register = template.Library()

@register.filter
def filename(path):
    """
    Extract the filename from a file path
    """
    return os.path.basename(path)
