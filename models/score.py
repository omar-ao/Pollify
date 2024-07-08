#!/usr/bin/python3
"""
Score model
"""


import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Score(BaseModel, Base):
    """Represents a Score"""
    __tablename__ = 'scores'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    quiz_id = Column(String(60), ForeignKey('quizzes.id'), nullable=False)
    score = Column(Float, nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes Score"""
        super().__init__(*args, **kwargs)
