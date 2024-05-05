from typing import List, Literal, Optional
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from pydantic import BaseModel, Field
from humps import camelize


def to_camel(string):
    return camelize(string)


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        populate_by_name = True


class EventDto(CamelModel):
    lat: Optional[float]
    long: Optional[float]


class UserCreateDto(EventDto):
    user_name: str
    user_password: str


class UserLoginDto(UserCreateDto):
    pass


class LocationUpdateDto(EventDto):
    user_name: str
