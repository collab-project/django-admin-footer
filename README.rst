django-admin-footer
===================

``django-admin-footer`` provides a templatetag that renders a footer with
version information in the Django admin.

.. image:: https://img.shields.io/pypi/v/django-admin-footer.svg
    :target: https://pypi.python.org/pypi/django-admin-footer
.. image:: https://img.shields.io/pypi/pyversions/django-admin-footer.svg
    :target: https://pypi.python.org/pypi/django-admin-footer
.. image:: https://travis-ci.org/collab-project/django-admin-footer.svg?branch=master
    :target: https://travis-ci.org/collab-project/django-admin-footer
.. image:: https://coveralls.io/repos/collab-project/django-admin-footer/badge.svg
    :target: https://coveralls.io/r/collab-project/django-admin-footer
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://raw.githubusercontent.com/collab-project/django-admin-footer/master/LICENSE

Installation
------------

Use pip_ to install the download and install the package from PyPi_::

  pip install django-admin-footer

Or checkout the source code from Github_::

  git clone https://github.com/collab-project/django-admin-footer.git
  cd django-admin-footer
  pip install -e .

Add ``admin_footer`` to ``INSTALLED_APPS`` in your Django project settings:

.. code-block:: python

  INSTALLED_APPS = (
      ...

      'admin_footer',
  )

Usage
-----

The ``ADMIN_FOOTER_DATA`` settings dict provides the data used in your footer.
The default template expects the following template vars: ``site_url``,
``site_name``, ``period`` and ``version``.

For example in ``settings.py``:

.. code-block:: python

  from datetime import datetime
  from myapp import version

  ADMIN_FOOTER_DATA = {
    'site_url': 'https://www.google.com',
    'site_name': 'Google',
    'period': '{}'.format(datetime.now().year),
    'version': 'v{} - '.format(version)
  }

Load the tag in your admin template (e.g. ``admin/base.html``):

.. code-block:: python

  {% load footer %}

And add the ``admin_footer`` tag to the ``footer`` block:

.. code-block:: python

  {% block footer %}
  {% admin_footer %}
  {% endblock %}

You'll now see a copyright link at the bottom of the admin pages.
The ``version`` information is hidden for non-staff users.

.. _pip: https://pypi.python.org/pypi/pip
.. _PyPi: https://pypi.python.org/pypi/django-admin-footer
.. _Github: https://github.com/collab-project/django-admin-footer
