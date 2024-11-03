from pydantic import BaseModel


class UserRegisterBody(BaseModel):
    phone_number: str
    email: str
    password: str
    confirm_password: str


class UserResponse(BaseModel):
    id: int
    phone_number: str
    email: str


class UserLoginBody(BaseModel):
    phone_number: str
    password: str
