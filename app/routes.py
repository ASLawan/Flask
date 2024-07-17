#!/usr/bin/env python3
"""
    Module implementing different URLs that the application
    supports

"""
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    """Default application route"""
    
    # mock objects
    user = {"username": "Lawan"}
    posts = [
            {
                'author': {'username': 'Lawan'},
                'body': 'How we won Camtel Tech Challenge'
            },
            {
                'author': {'username': 'Laiven'},
                'body': 'How we won Total Energies Challenge'
            },
            {
                'author': {'username': 'Austin'},
                'body': 'How we built TrAvel to a giant Tech company'
            }
            ]
    return render_template('index.html', title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Handles login"""
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
