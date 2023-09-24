#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes and stores user information"""

    __tablename__ = 'users'

   """This class defines a user by various attributes"""

    email = Column(String(128), nullable=False) 
    password = Column(String(128), nullable=False)
    first_name = Column(String(128)
    last_name = Column(String(128)
    places = relationship("Place", back_reference="user", cascade="delete")
    reviews = relationship("Review", back_reference="user", cascade="delete")
