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
url('/about', '_index.about')
url('/baiduMap', '_index.baiduMap')
url('/case', '_index.case')
url('/contacts', '_index.contacts')
url('/join', '_index.join')
url('/pricing', '_index.pricing')
url('/products', '_index.products')
url('/reports', '_index.reports')
url('/signup', '_index.signup')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
