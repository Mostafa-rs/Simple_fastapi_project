from fastapi import APIRouter, Depends

from accounts import apis
from utils.auth import JWTBearer

router = APIRouter()

router.add_api_route('/user/info', apis.UserInfoAPI().get, methods=['GET'], dependencies=[Depends(JWTBearer)])
router.add_api_route('/list', apis.UserAPI().get, methods=['GET'], dependencies=[Depends(JWTBearer())])
router.add_api_route('/register', apis.UserAPI().post, methods=['POST'])
router.add_api_route('/login', apis.UserLoginAPI().post, methods=['POST'])

