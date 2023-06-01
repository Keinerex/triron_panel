from datetime import timedelta

from config import get_settings
from utils import authenticate_user, create_access_token

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from db.connection import get_session
from schemas import Token

api_router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@api_router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=Token
)
async def authentication(
        _: Request,
        form_data: OAuth2PasswordRequestForm = Depends(),
        session: AsyncSession = Depends(get_session)
):
    if not authenticate_user(username=form_data.username, password=form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=get_settings().ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": form_data.username},
                                       expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
