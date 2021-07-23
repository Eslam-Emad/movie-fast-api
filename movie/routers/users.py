from fastapi import APIRouter ,Depends
from sqlalchemy.orm.session import Session
from .. import schemas  
from .. database import get_db
from ..repository import  users
from movie.oauth2 import get_current_user



router = APIRouter(tags=['user'], prefix="/user")



@router.get('/{id}' ,response_model= schemas.showUser )
def get_user(id, db:Session = Depends(get_db) ,current_user:schemas.User = Depends(get_current_user)):
    return users.get_user(id=id , db=db)



@router.put('/{id}' ,response_model= schemas.showUser)
def update_user(
    id, request:schemas.User,
    db:Session = Depends(get_db),
    current_user:schemas.User = Depends(get_current_user)
    ):
    return users.update_user(id=id ,request=request, db=db)
   
