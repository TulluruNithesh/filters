from django import template
register=template.Library()

@register.filter(name='low')
def lower(value):
    return value.lower()

@register.filter(name='replace')
def replace_char(value,arg):
    return value.replace(arg,'b')

@register.filter()
def remove(value,arg):
    return value.replace(arg,'')
@register.filter()
def count(value,arg):
    s=arg
    c=0
    l
    for i in range(len(value)-len(s)+1):
        if ==s:
            c+=1
    return c



#register.filter('low',lower)
#register.filter('rep',replace_char)