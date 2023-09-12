from django import template
from talentsystem.encryption import encrypt_data

register = template.Library()
formart= "|encrypt"
@register.filter
def encrypt(value):
    return encrypt_data(value)