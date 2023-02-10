#!/usr/bin/python3
"""Defines Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents Amenity

    Attributes:
        name(str) - name of Amenity
    """
    name = ""
