#!/usr/bin/python3
"""
Vote model
"""


import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Vote(BaseModel, Base):
    """Represents a vote"""
    __tablename__ = 'votes'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    poll_id = Column(String(60), ForeignKey('polls.id'), nullable=False)
    option_id = Column(String(60), ForeignKey('options.id'), nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes poll"""
        super().__init__(*args, **kwargs)
