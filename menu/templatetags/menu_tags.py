from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    try:
        menu = MenuItem.objects.get(name=menu_name)
        return menu.render_menu()
    except MenuItem.DoesNotExist:
        return f"Menu '{menu_name}' not found"
