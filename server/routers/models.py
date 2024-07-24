from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DATE
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    firstName = Column(String)
    lastName = Column(String)
    middleName = Column(String, nullable=True)
    dob = Column(DATE)
    phone = Column(Integer)
    gender = Column(String)
    address = Column(String)
    pincode = Column(Integer)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    areaOfInterst = Column(String)