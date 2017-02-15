#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask

import src
from src._error import error_404
from src._helpers import LazyView

app = Flask(__name__)


def url(url_rule, import_name, **options):
    view = LazyView('src.'+import_name)
    app.add_url_rule(url_rule, view_func=view, **options)
    app.add_url_rule(url_rule+'.html', view_func=view, **options)

app.register_error_handler(404, error_404)
url('/', '_index.homepage')
url('/blog', '_index.blog')
url('/login', '_index.login')
url('/logout', '_index.logout')
url('/landing', '_index.landing')
url('/iscroll', '_index.iscroll')
url('/non-responsive', '_index.non_responsive')
url('/sidebar', '_index.sidebar')
url('/widget', '_index.widget')
url('/widget-basic', '_index.widget_basic')
url('/admin-404', '_index.admin_404')
url('/admin-form', '_index.admin_form')
url('/admin-gallery', '_index.admin_gallery')
url('/admin-help', '_index.admin_help')
url('/admin-index', '_index.admin_index')
url('/admin-log', '_index.admin_log')
url('/admin-table', '_index.admin_table')
url('/admin-user', '_index.admin_user')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
