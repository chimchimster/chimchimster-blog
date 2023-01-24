from django import template

register = template.Library()

@register.inclusion_tag('blog/menu.html')
def main_menu():
    menu = [
        {'title': 'Articles', 'url_name': 'articles'},
        {'title': 'Add Article', 'url_name': 'add_article'},
        {'title': 'Portfolio', 'url_name': 'portfolio'},
        {'title': 'Sign In', 'url_name': 'login'}
    ]

    return {'menu': menu}