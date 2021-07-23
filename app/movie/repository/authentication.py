from datetime import timedelta
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from starlette import status
from movie import models,schemas 
from movie.JWT import *
from movie.database import get_db
from movie.hash import Hash



def register(request:schemas.User, db:Session = Depends(get_db)):
    hashed_password = Hash.bcrybt(request.password)
    new_user = models.User(name=request.name , email=request.email , password= hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




def login(request:OAuth2PasswordRequestForm = Depends(),  db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user :
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f'Invaild Credentials')

    if not Hash.verify(request.password , user.password):
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f'Incorrect Password')

    # generate JWT  
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token( 
        data= {"sub": user.email}, expires_delta=access_token_expires
         )
    return {
        "id": user.id,
        "email": user.email,
        "access_token": access_token, 
        "token_type": "bearer"
        }