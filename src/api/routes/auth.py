from typing import Annotated  # noqa: I001

from fastapi import APIRouter, Depends, Request, Response
from fastapi.security import OAuth2PasswordRequestForm

from ..exceptions import InvalidTokenException
from ..dependencies import UnitOfWorkContext
from ...core import settings as config
from ...infrastructure.db.services import service
from ..schemas import Token

router = APIRouter()


@router.post("/login", response_model=Token)
async def access_token(
    response: Response,
    uow: UnitOfWorkContext,
    *,
    credentials: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    token = await service.auth.authenticate_user(
        uow, email=credentials.username, password=credentials.password
    )

    response.set_cookie(
        "refresh_token",
        token.refresh_token,
        max_age=config.auth.REFRESH_TOKEN_EXPIRE_DAYS * 60 * 60 * 24,
        httponly=True,
    )

    return token


@router.post("/refresh", response_model=Token)
async def refresh_access_token(
    request: Request,
    uow: UnitOfWorkContext,
) -> Token:
    refresh_token = request.cookies.get("refresh_token")

    if not refresh_token:
        raise InvalidTokenException

    return await service.auth.refresh_token(uow, refresh_token=refresh_token)


@router.post("/logout")
async def logout(
    request: Request,
    response: Response,
    uow: UnitOfWorkContext,
) -> None:
    refresh_token = request.cookies.get("refresh_token")

    if not refresh_token:
        raise InvalidTokenException

    response.delete_cookie("refresh_token", httponly=True)

    await service.auth.logout(uow, refresh_token=refresh_token)
