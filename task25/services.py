from models.models import User, UserRate, Apartment, Booking


async def create_user(db, schema):
    user = User(**schema.dict())

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


async def delete_user(db, user) -> None:
    db.delete(user)
    db.commit()


async def update_user(db, user, schema):
    for key, value in schema.dict().items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user


async def retrieve_user_by_username(db, username: str):
    return db.query(User).filter_by(username=username).first()


async def retrieve_user_by_id(db, id: int):
    return db.query(User).filter_by(id=id).first()

#UserRate


async def create_user_rate(db, schema):
    user = UserRate(**schema.dict())

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


async def retrieve_user_rate_by_id(db, id: int):
    return db.query(UserRate).filter_by(id=id).first()

#Apartments


async def create_apartments(db, schema):
    apartments = Apartment(**schema.dict())

    db.add(apartments)
    db.commit()
    db.refresh(apartments)

    return apartments


async def retrieve_apartments(db, id: int):
    return db.query(Apartment).filter_by(id=id).first()

#Booking


async def create_booking(db, schema):
    booking = Booking(**schema.dict())

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking


async def retrieve_booking(db, id: int):
    return db.query(Booking).filter_by(id=id).first()