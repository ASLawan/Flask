#!/usr/bin/env python3
"""
    Module implementing basic Flask application

"""
from flask import Flask


app = Flask(__name__)

from app import routes
