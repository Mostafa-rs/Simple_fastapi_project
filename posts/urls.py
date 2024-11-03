from fastapi import APIRouter

from posts import apis
from posts.rr_defines import PostResponse

router = APIRouter()

router.add_api_route('/list', apis.PostAPI().get, methods=['GET'])
router.add_api_route('/create', apis.PostAPI().post, methods=['POST'], response_model=PostResponse)


