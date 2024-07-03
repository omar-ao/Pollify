#!/usr/bin/python3
"""
Renders home page
"""

from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def index():
    """Renders index page"""
    return "Pollify home page"

