from datetime import timedelta, datetime

from config import get_settings

from jose import jwt


def authenticate_user(
        username: str,
        password: str,
) -> bool:
    return (username, password) == get_settings().auth_data


def create_access_token(
        data: dict,
        expires_delta: timedelta | None = None,
):
    settings = get_settings()
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
