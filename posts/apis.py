from sqlmodel import Session, select
from fastapi import Depends, FastAPI, Body, Query

from posts.models import Post
from db import get_session
from posts.rr_defines import PostBody, PostResponse
from utils.response import get_response


class PostAPI:
    async def get(self, session: Session = Depends(get_session)):
        res = session.query(Post).all()
        return get_response([PostResponse(id=obj.id, title=obj.title, content=obj.content).dict() for obj in res])

    async def post(self, post_data: PostBody = Body(), session: Session = Depends(get_session)):
        if session.query(Post).get(post_data.id):
            pk = post_data.id
            return {'detail': f'post with id {pk = } exists'}

        post = Post(id=post_data.id, title=post_data.title, content=post_data.content)
        session.add(post)
        session.commit()
        session.refresh(post)
        return post
