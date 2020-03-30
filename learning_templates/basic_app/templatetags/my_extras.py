from django import template

register = template.Library()

#This is one way to do it and it uses something that is called decorators
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

    
# This is one way to do it and it is more clear
# def cut(value, arg):
#     """
#     This cuts out all valus of "arg" from the string!
#     """
#     return value.replace(arg,'')
#
# register.filter('cut',cut)
