from fastapi import Body, Depends, Form, Header, APIRouter
from sqlalchemy.orm import Session

from accounts.rr_defines import UserRegisterBody, UserResponse, UserLoginBody
from db import get_session
from utils.response import get_response
from accounts.models import User
from utils.auth import hash_password, verify_password
from accounts.validations import user_register_validation, phone_number_validation
from utils import auth
from utils.decorators import check_roles


class UserInfoAPI:
    def get(self, session: Session = Depends(get_session), Authorization: str = Header()):
        user_id = auth.get_current_user_id(Authorization[7:])
        user = session.query(User).get(user_id)

        return get_response(UserResponse(**dict(user)).dict())


class UserAPI:
    async def get(self, pk: int = None, session: Session = Depends(get_session)):
        if pk:
            if not session.query(User).get(pk):
                return get_response(errors={'detail': f'user with {pk=} not found'}, status_code=404)

            user = User(**dict(session.query(User).get(pk)))

            return get_response(UserResponse(**user.dict()).dict())
        else:
            return get_response([UserResponse(**user.dict()).dict() for user in session.query(User).all()])

    async def post(self, user_data: UserRegisterBody = Form(), session: Session = Depends(get_session)):
        """
        Register user
        :param user_data:
        :return:
        """
        errors = user_register_validation(user_data, session)

        if errors:
            return get_response(errors=errors)

        user = User(phone_number=user_data.phone_number, email=user_data.email,
                    password=hash_password(user_data.password))
        session.add(user)
        session.commit()
        session.refresh(user)

        return get_response(UserResponse(**user.dict()).dict())


class UserLoginAPI:
    async def post(self, user_data: UserLoginBody = Form(), session: Session = Depends(get_session)):
        errors = phone_number_validation(user_data.phone_number)

        if errors:
            return get_response(errors=errors)

        if not session.query(User).filter_by(phone_number=user_data.phone_number):
            return get_response(errors={'detail': 'phone number or password is wrong'}, status_code=404)

        user = session.query(User).filter_by(phone_number=user_data.phone_number).first()
        password_check = verify_password(user_data.password, user.password)

        if not password_check:
            return get_response(errors={'detail': 'phone number or password is wrong'}, status_code=404)

        token, exp_time = auth.get_token(str(user.id))

        return get_response({'token': token, 'expires_in': f'{exp_time}'})





