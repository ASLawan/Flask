#!/usr/bin/env python3
"""
    Module implementing basic Flask application

"""
from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

from app import routes
