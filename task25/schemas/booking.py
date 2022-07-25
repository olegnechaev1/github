from pydantic import BaseModel
from datetime import datetime


class BookingCreateSchema(BaseModel):
    user_id: int
    apartment_id: int
    
    
class BookingRetrieveSchema(BaseModel):
    id: int
    user_id: int
    apartment_id: int
    created_date: datetime
    
    class Config:
        orm_mode = True