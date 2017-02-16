#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import render_template, url_for, redirect


def homepage():
    return render_template('index.html')


def about():
    return render_template('about.html')


def baiduMap():
    return render_template('baiduMap.html')


def logout():
    return redirect(url_for('homepage'), 301)


def case():
    return render_template('case.html')


def contacts():
    return render_template('contacts.html')


def join():
    return render_template('join.html')


def pricing():
    return render_template('pricing.html')


def products():
    return render_template('products.html')


def reports():
    return render_template('reports.html')


def signup():
    return render_template('signup.html')
