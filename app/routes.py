#!/usr/bin/env python3
"""
    Module implementing different URLs that the application
    supports

"""
from flask import render_template
from app import app


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
