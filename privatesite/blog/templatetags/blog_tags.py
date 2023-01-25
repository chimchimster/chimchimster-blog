from django import template

register = template.Library()

@register.inclusion_tag('blog/menu.html')
def main_menu():
    menu = [
        {'title': 'Portfolio', 'url_name': 'portfolio'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Sign In', 'url_name': 'login'}
    ]

    return {'menu': menu}