from flask import Blueprint, render_template
from flask import redirect, url_for, flash, request
from app import bcrypt, login_manager
from models import storage
from models.user import User
from flask_login import (login_user, current_user, logout_user,
                         login_required)
from app.forms import LoginForm, RegistrationForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # TODO: Implement authentication logic
    #if current_user.is_authenticated:
    #    return redirect(url_for('poll.create_poll'))
    form = LoginForm()
    if form.validate_on_submit():
        user = storage.get_session().query(User).filter_by(
                email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home.index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('/login.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('poll.create_poll'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user_data = {
                'first_name': form.first_name.data,
                'last_name': form.last_name.data,
                'email': form.email.data,
                'password': form.password.data
                }
        user = User(**user_data)
        user.save()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    print(user_id)
    return storage.get(User, user_id)
