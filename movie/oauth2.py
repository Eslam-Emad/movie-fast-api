from movie.JWT import ALGORITHM , SECRET_KEY
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from .JWT import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token: str = Depends(oauth2_scheme)):

    return await verify_token(token=token)
    
