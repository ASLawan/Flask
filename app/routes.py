#!/usr/bin/env python3
"""
    Module implementing different URLs that the application
    supports

"""
from app import app

@app.route('/')
@app.route('/index')
def index():
    """Default application route"""
    return "Hello from the other side!"
