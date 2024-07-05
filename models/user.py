#!/usr/bin/python3
"""
User model
"""

import bcrypt
import models
from models.base_model import BaseModel, Base
from models.poll import Poll
import sqlalchemy
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    polls = relationship('Poll', backref='user')
    status = Column(Boolean, default=True)

    def __init__(self, *args, **kwargs):
        """User initialization"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, key, value):
        """
        If the key is password, set the password with bcrypt encryption
        """
        if key == "password":
            value = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        super().__setattr__(key, value)

    def check_password(self, password):
        """
        Check hashed password.
        """
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def activate(self):
        """
        Activates a user
        """
        self.status = True

    def deactivate(self):
        """
        Deactivates a user
        """
        self.status = False

    @property
    def is_active(self):
        """
        Checks whether a user is active
        """
        return self.status
    
    @property
    def is_authenticated(self):
        """
        Checks whether the user is authenticated
        """
        # TODO: Add authentication logic
        return True

    def get_id(self):
        """
        Return the unique identifier for the user (typically 'id' or 'email').
        """
        return str(self.id)
