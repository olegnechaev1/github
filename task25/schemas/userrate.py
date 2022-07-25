from pydantic import BaseModel


class UserRateCreateSchema(BaseModel):
    comment: str
    stars: str
    user_id: int
    
    
class UserRateRetrieveSchema(BaseModel):
    id: int
    comment: str
    user_id: int
    
    class Config:
        orm_mode = True