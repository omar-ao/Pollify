#!/usr/env/bin python
"""
Contains Quiz model
"""


from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, JSON
from sqlalchemy.orm import relationship


class Quiz(BaseModel, Base):
    """Represents a quiz"""
    __tablename__ = 'quizzes'
    title = Column(String(200), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    questions = Column(JSON, nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes quiz"""
        super().__init__(*args, **kwargs)
