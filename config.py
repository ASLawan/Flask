#!/usr/bin/env python3
""""
    Module implementing Config class

"""
import os


class Config:
    """Class handling app configurations"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
