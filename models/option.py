#!/usr/bin/python3
"""
Option model
"""


import models
from models.base_model import BaseModel, Base
from models.vote import Vote
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Option(BaseModel, Base):
    """Represents an option"""
    __tablename__ = 'options'
    text = Column(String(200), nullable=False)
    poll_id = Column(String(60), ForeignKey('polls.id'), nullable=False)
    votes = relationship('Vote', backref='option')


    def __init__(self, *args, **kwargs):
        """initializes poll"""
        super().__init__(*args, **kwargs)
