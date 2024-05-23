from django import template

register = template.Library()

@register.filter
def english_number_to_persion(value):
    value = str(value)
    english_to_persion = value.maketrans('0123456789',"۰۱۲۳۴۵۶۷۸۹")
    return value.translate(english_to_persion)