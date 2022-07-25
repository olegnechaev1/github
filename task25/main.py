import time

from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from jwt_bearer import jwtBearer
from database.database import SessionLocal, engine
from models import models
from schemas.apartments import ApartmentCreateSchema, ApartmentRetrieveSchema
from schemas.booking import BookingCreateSchema, BookingRetrieveSchema
from schemas.userrate import UserRateCreateSchema, UserRateRetrieveSchema
from schemas.users import (UsersCreateSchema, UsersRetrieveSchema,
                           UsersUpdateSchema, UsersLoginSchema)
from services import (create_user, create_user_rate, delete_user,
                      retrieve_user_by_id, retrieve_user_by_username,
                      retrieve_user_rate_by_id, update_user,
                      create_apartments, retrieve_apartments,
                      create_booking, retrieve_booking
                      )

from jwt_handler import signJWT

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def write_notification(email: str, message=""):
    time.sleep(5)
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post('/users/signup', response_model=UsersRetrieveSchema,
          status_code=status.HTTP_201_CREATED)
async def create(schema: UsersCreateSchema, background_tasks: BackgroundTasks,
                 db: Session = Depends(get_db)):
    user = await retrieve_user_by_username(db, schema.dict()['username'])
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='User already exists.')

    else:
        user = await create_user(db, schema)

    background_tasks.add_task(
        write_notification,
        email=user.email,
        message=f"Hello {user.username}, Welcome!"
    )
    return user


@app.post('/users/login', status_code=status.HTTP_201_CREATED)
async def create_user_login(schema: UsersLoginSchema, db: Session = Depends(get_db)):
    if user := await retrieve_user_by_username(db, schema.dict()['username']):
        return signJWT(user.username)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get('/users/{id}', response_model=UsersRetrieveSchema)
async def get_user(id: int, db: Session = Depends(get_db)):
    if user := await retrieve_user_by_id(db, id):
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.put('/users/{id}', response_model=UsersRetrieveSchema,
         status_code=status.HTTP_200_OK)
async def update_users(id: int, schema: UsersUpdateSchema,
                       db: Session = Depends(get_db)):
    if user := await retrieve_user_by_id(db, id):
        user = await update_user(db, user, schema)
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int, db: Session = Depends(get_db)):
    if user := await retrieve_user_by_id(db, id):
        await delete_user(db, user)
        return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#UserRate


@app.post('/users-rate/', dependencies=[Depends(jwtBearer())], 
          response_model=UserRateRetrieveSchema,
          status_code=status.HTTP_201_CREATED)
async def create_rate(schema: UserRateCreateSchema, db: Session = Depends(get_db)):
    user = await create_user_rate(db, schema)
    return user


@app.get('/users-rate/{id}', response_model=UserRateRetrieveSchema)
async def get_user_rate(id: int, db: Session = Depends(get_db)):
    if user := await retrieve_user_rate_by_id(db, id):
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#Apartments


@app.post('/apartments/', response_model=ApartmentRetrieveSchema,
          status_code=status.HTTP_201_CREATED)
async def create_apartment(schema: ApartmentCreateSchema,
                           db: Session = Depends(get_db)):
    apartments = await create_apartments(db, schema)
    return apartments


@app.get('/apartments/{id}', response_model=ApartmentRetrieveSchema)
async def get_apartment(id: int, db: Session = Depends(get_db)):
    if apartments := await retrieve_apartments(db, id):
        return apartments
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#Booking


@app.post('/booking/', response_model=BookingRetrieveSchema,
          status_code=status.HTTP_201_CREATED)
async def create_bookings(schema: BookingCreateSchema,
                          db: Session = Depends(get_db)):
    apartments = await create_booking(db, schema)
    return apartments


@app.get('/booking/{id}', response_model=BookingRetrieveSchema)
async def get_booking(id: int, db: Session = Depends(get_db)):
    if apartments := await retrieve_booking(db, id):
        return apartments
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)