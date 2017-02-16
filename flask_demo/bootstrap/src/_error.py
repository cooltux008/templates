#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import render_template


def error_404(e):
    return render_template('admin-404.html'), 404
