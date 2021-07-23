from fastapi import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from starlette import status
from movie import schemas , models 
from movie.database import get_db



def get_user(id, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f'there is no user with this id {id}')
    return user



def update_user(id, request:schemas.User ,  db:Session = Depends(get_db)):
    updated_user =  db.query(models.User).filter(models.User.id == id).update(request)
    db.commit()
    if not updated_user:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f'there is no user with this id {id}')
    return update_user
