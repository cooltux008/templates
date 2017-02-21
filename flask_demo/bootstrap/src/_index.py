#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import render_template, url_for, redirect


def homepage():
    return render_template('index.html')


def admin():
    return render_template('admin.html')


def blog():
    return render_template('blog.html')


def login():
    return render_template('login.html')


def logout():
    return redirect(url_for('homepage'), 301)
