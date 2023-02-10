#!/usr/bin/python3
"""Defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents User instance

    Attributes:
        email(str) - user email
        password(str) - user password
        first_name(str) - user first name
        last_name(str) - user last name
    """
    password = ""
    first_name = ""
    last_name = ""
