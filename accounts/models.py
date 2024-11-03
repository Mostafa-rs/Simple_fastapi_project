from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int = Field(primary_key=True, unique=True)
    phone_number: str = Field(nullable=False)
    email: str = Field(nullable=True, unique=True)
    password: str = Field(nullable=True)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    is_staff: bool = Field(default=False)
