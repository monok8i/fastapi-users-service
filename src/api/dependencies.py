from typing import Annotated  # noqa: I001

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from core import settings as config
from infrastructure.db.uow import UnitOfWork
from infrastructure.db.models import User
from infrastructure.db.services import service
from schemas.token import TokenPayload

from .exceptions import InvalidTokenException


# unit of work context
UnitOfWorkContext = Annotated[UnitOfWork, Depends(UnitOfWork)]

# reusable URL for receiving auth token from user
oauth2 = OAuth2PasswordBearer(tokenUrl=f"{config.common.API_V1}/auth/login")

# put auth token in variable using Annotated special form
TokenDep = Annotated[str, Depends(oauth2)]


async def get_current_user(
    uow: UnitOfWorkContext, _token: TokenDep
) -> User | HTTPException:
    try:
        payload = service.auth.decode_jwt_token(token=_token)
        token_data: TokenPayload = TokenPayload(**payload)  # type: ignore
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    user = await service.user.get_by_id(uow, user_id=token_data.sub)  # type: ignore

    if not user:
        raise InvalidTokenException

    return user


# put result of function in variable using `Annotated` special form
CurrentUser = Annotated[User, Depends(get_current_user)]
