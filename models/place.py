#!/usr/bin/python3
"""DEfines Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents Place

    Attributes:
        city_id(str) - city id
        user_id(str) - user id
        name(str) - name
        description(str) - description
        number_rooms(int) - number of rooms
        number_bathrooms(int) - number of rooms
        max_guest(int) - maximum guests
        price_by_night(int) - price per night
        latitude(float) - coordinates
        longitude(float) - coorinates
        amenity_ids(str) - list of amenity id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
