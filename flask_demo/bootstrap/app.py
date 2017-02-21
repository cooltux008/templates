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
url('/login', '_index.login')
url('/register', '_index.register')
url('/admin', '_index.admin')
url('/blog', '_index.blog')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
