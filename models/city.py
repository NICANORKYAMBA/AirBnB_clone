#!/usr/bin/python3
"""Defines City class"""
from models.base_model import Base_Model


class City(BaseModel):
    """Represents city

    Attributes:
        state_id(str) - state's id
        name(str) - name of the city
    """
    state_id = ""
    name = ""
