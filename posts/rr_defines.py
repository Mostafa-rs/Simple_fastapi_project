from pydantic import BaseModel


class PostBody(BaseModel):
    id: int
    title: str
    content: str | None


class PostResponse(BaseModel):
    id: int
    title: str
    content: str | None
