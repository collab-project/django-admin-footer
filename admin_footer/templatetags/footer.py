# Copyright Collab 2015-2016
# See LICENSE for details.

"""
Admin footer template tag.
"""

from datetime import datetime

from django import template
from django.conf import settings
from django.template import base, loader


register = template.Library()


class AdminFooterNode(template.Node):
    """
    Build footer and render the resulting context into the template.
    """
    def render(self, context):
        data = getattr(settings, 'ADMIN_FOOTER_DATA', {
            'period': datetime.now().year
        })
        if context['request'].user.is_staff is False:
            data.pop('version', None)

        tpl = loader.get_template('admin_footer/footer.html')
        return tpl.render(data)


@register.tag
def admin_footer(parser, token):
    """
    Template tag that renders the footer information based on the
    authenticated user's permissions.
    """
    # split_contents() doesn't know how to split quoted strings.
    tag_name = token.split_contents()

    if len(tag_name) > 1:
        raise base.TemplateSyntaxError(
            '{} tag does not accept any argument(s): {}'.format(
            token.contents.split()[0],
            ', '.join(token.contents.split()[1:])
    ))

    return AdminFooterNode()
