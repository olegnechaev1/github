from pydantic import BaseModel
from typing import List
from schemas.booking import BookingRetrieveSchema


class ApartmentCreateSchema(BaseModel):
    city: str
    hotel: str
    room: int
    cost: int
    user_id: int
    

class ApartmentRetrieveSchema(BaseModel):
    id: int
    city: str
    hotel: str
    room: int
    cost: int
    user_id: int
    bookings_apartment: List[BookingRetrieveSchema] = []
    
    class Config:
        orm_mode = True