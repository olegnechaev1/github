import enum
from sqlalchemy.sql import func
from database.database import Base
from sqlalchemy import (Boolean, Column, Enum, ForeignKey,
                        Integer, String, DateTime)
from sqlalchemy.orm import relationship


class Status(enum.Enum):
    Host = "Host"
    User = "User"
        

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    role = Column(Enum("Host", "User", name=Status), default="User")
    apartments = relationship("Apartment", back_populates="user")
    bookings_user = relationship("Booking", back_populates="user")
    
    
class Stars(enum.Enum):
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"    
    
    
class UserRate(Base):
    __tablename__ = 'UserRates'

    id = Column(Integer, primary_key=True)
    comment = Column(String(200))
    stars = Column(Enum("1", "2", "3", "4", "5", name=Stars), default=5)
    user_id = Column(Integer, ForeignKey("users.id"))
        

class Apartment(Base):
    __tablename__ = 'Apartments'
    
    id = Column(Integer, primary_key=True)
    city = Column(String(50))
    hotel = Column(String(50))
    room = Column(Integer)
    cost = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="apartments")
    bookings_apartment = relationship("Booking", back_populates="apartment")
    
    
class Booking(Base):
    __tablename__ = 'Bookings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    apartment_id = Column(Integer, ForeignKey("Apartments.id"))
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="bookings_user")
    apartment = relationship("Apartment", back_populates="bookings_apartment")