#!/usr/bin/python3
"""This is the Amenity class."""
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel


class Amenity(BaseModel, Base):
    """shows an Amenity for a MySQL databe
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
