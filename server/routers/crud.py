from sqlalchemy.orm import Session
from . import models,schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(email=user.email, 
                          hashed_password=hashed_password, 
                          is_active = user.is_active,
                          firstName = user.firstName,
                          lastName = user.lastName,
                          middleName = user.middleName,
                          dob = user.dob,
                          phone = user.phone,
                          gender = user.gender,
                          address = user.address,
                          pincode = user.pincode,
                          city = user.city,
                          state = user.state,
                          country = user.country,
                          areaOfInterst = user.areaOfInterst)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user
