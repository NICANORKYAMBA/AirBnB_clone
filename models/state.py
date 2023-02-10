#!/usr/bin/python3
"""Defines a State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """REpresents a State

    Attributes:
        name(str) - name state
    """
    name = ""
