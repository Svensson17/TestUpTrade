from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True, related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def render_menu(self):
        html = ''
        html += self._render_subtree()
        return html

    def _render_subtree(self):
        html = ''
        for child in self.get_children():
            html += '<li>'
            html += f'<a href="{child.url}">{child.name}</a>'
            if child.get_children():
                html += '<ul>'
                html += child._render_subtree()
                html += '</ul>'
            html += '</li>'
        return html
