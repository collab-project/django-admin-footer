# Copyright Collab 2015-2016
# See LICENSE for details.

"""
Tests for the :py:mod:`admin_footer` templatetag.
"""

from __future__ import unicode_literals

from django.conf import settings
from django.template import base, loader
from django.template.context import Context
from django.test import TestCase, RequestFactory

from django.contrib.auth.models import User


class FooterTagTests(TestCase):
    """
    Tests for the :py:mod:`~admin_footer.templatetags.footer` template tag.
    """
    def _renderTemplate(self, version=False):
        data = settings.ADMIN_FOOTER_DATA
        if version is True:
            data.pop('version', None)
        tpl = loader.get_template('admin_footer/footer.html')
        return tpl.render(data)

    def assertFooter(self, context, output,
                     template='{% admin_footer %}'):
        """
        :param template:
        :param context:
        :param output:
        """
        template = base.Template('{% load footer %}' + template)
        ctx = Context(context)
        self.assertEqual(template.render(ctx), output)

    def test_footerAuthenticated(self):
        """
        Using the tag with admin rights returns the footer with a version nr.
        """
        user = User.objects.create_superuser('test',
            'test@koo.ls', 'top_secret')
        request = RequestFactory().post('/', user=user)
        request.user = user
        context = {'request': request}
        output = self._renderTemplate()

        self.assertFooter(context, output)

    def test_footerAnonymous(self):
        """
        Using the tag as anonymous user excludes the version nr in the footer.
        """
        user = User.objects.create_user('test',
            'test@koo.ls', 'top_secret')
        request = RequestFactory().post('/', user=user)
        request.user = user
        context = {'request': request}
        output = self._renderTemplate(True)

        self.assertFooter(context, output)

    def test_rejectArguments(self):
        """
        Passing arguments to the tag raises a `TemplateSyntaxError`.
        """
        try:
            base.Template('{% load footer %}{% admin_footer foo %}')
        except base.TemplateSyntaxError as e:
            self.assertEqual(str(e),
                'admin_footer tag does not accept any argument(s): foo')
