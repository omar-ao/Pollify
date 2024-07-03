#!/usr/bin/python3
"""
Poll model
"""


import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Poll(BaseModel, Base):
    """Represents a poll"""
    __tablename = 'polls'
    title = Column(db.String(200), nullable=False)
    user_id = Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    options = relationship('Option', backref='poll')


    def __init__(self, *args, **kwargs):
        """initializes poll"""
        super().__init__(*args, **kwargs)
