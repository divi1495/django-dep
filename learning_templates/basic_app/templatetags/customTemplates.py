from django import template

register = template.Library()

@register.filter(name='cut')
def cut(variable,arg):
    # This cuts out all values of arg from the string
    return variable.replace(arg,"")


# register.filter('cut',cut)