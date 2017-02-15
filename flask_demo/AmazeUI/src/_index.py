#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import render_template, url_for, redirect


def homepage():
    return render_template('index.html')


def blog():
    return render_template('blog.html')


def login():
    return render_template('login.html')


def logout():
    return redirect(url_for('homepage'), 301)


def landing():
    return render_template('landing.html')


def iscroll():
    return render_template('iscroll.html')


def non_responsive():
    return render_template('non-responsive.html')


def sidebar():
    return render_template('sidebar.html')


def widget():
    return render_template('widget.html')


def widget_basic():
    return render_template('widget.basic.html')


def admin_404():
    return render_template('admin-404.html')


def admin_form():
    return render_template('admin-form.html')


def admin_gallery():
    return render_template('admin-gallery.html')


def admin_help():
    return render_template('admin-help.html')


def admin_index():
    return render_template('admin-index.html')


def admin_log():
    return render_template('admin-log.html')


def admin_table():
    return render_template('admin-table.html')


def admin_user():
    return render_template('admin-user.html')
