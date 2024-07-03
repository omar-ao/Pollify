#!/usr/bin/python3
from flask import (Blueprint, render_template, redirect,
                   url_for, flash, request)
from flask_login import current_user, login_required

poll = Blueprint('poll', __name__)

@poll.route('/create_poll', methods=['GET', 'POST'])
@login_required
def create_poll():
    if request.method == 'POST':
        # logic to create poll
        pass
    return render_template('create_poll.html')

@poll.route('/poll_details/<int:poll_id>')
@login_required
def poll_details(poll_id):
    # logic to get poll details
    return render_template('poll_details.html')

@poll.route('/poll_results/<int:poll_id>')
@login_required
def poll_results(poll_id):
    # logic to get poll results
    return render_template('poll_results.html')

