#!/usr/bin/python3
"""
User model
"""

import models
from models.base_model import BaseModel, Base
from models.poll import Poll
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    polls = relationship('Poll', backref='user')

    def __init__(self, *args, **kwargs):
        """User initialization"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, key, value):
        """
        If the key is password, set the password with md5 encryption
        """
        if key == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(key, value)
