from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Post(SQLModel, table=True):
    id: int = Field(primary_key=True, unique=True)
    title: str = Field(max_length=100)
    content: str | None = Field(max_length=1000)

