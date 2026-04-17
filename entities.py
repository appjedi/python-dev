

import datetime

from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: str
    password: str
    created: str
    role_id: int
    status: int
class ContactUS(BaseModel):
    contactId: int
    fullName: str
    email: str
    phone: str
    message: str
    received: datetime.datetime

class Auth(BaseModel):
    username: str
    password: str