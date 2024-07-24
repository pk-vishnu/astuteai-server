from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    is_active: bool
    firstName: str
    lastName: str
    middleName: Optional[str]
    dob: date
    phone: int
    gender: str
    address: str
    pincode: int
    city: str
    state: str
    country: str
    areaOfInterst: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
        

