from pydantic import BaseModel
from typing import List
from schemas.apartments import ApartmentRetrieveSchema
from schemas.booking import BookingRetrieveSchema


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class UsersCreateSchema(BaseModel):
    email: str
    username: str
    password: str
    role: str


class UsersUpdateSchema(BaseModel):
    email: str
    username: str
    password: str
    role: str
    
    
class UsersLoginSchema(BaseModel):
    username: str
    password: str    


class UsersRetrieveSchema(BaseModel):
    id: int
    email: str
    username: str
    password: str
    role: str
    apartments: List[ApartmentRetrieveSchema] = []
    bookings_user: List[BookingRetrieveSchema] = []
    
    class Config:
        orm_mode = True
