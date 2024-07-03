#!/usr/bin/python3
"""
Poll model
"""


import models
from models.base_model import BaseModel, Base
from models.option import Option
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Poll(BaseModel, Base):
    """Represents a poll"""
    __tablename__ = 'polls'
    title = Column(String(200), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    options = relationship('Option', backref='poll')


    def __init__(self, *args, **kwargs):
        """initializes poll"""
        super().__init__(*args, **kwargs)
