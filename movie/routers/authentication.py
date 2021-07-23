from fastapi import APIRouter ,Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from .. import schemas  
from .. database import get_db
from ..repository import  users ,authentication


router = APIRouter(tags=['authentication'])


@router.post("/register" , response_model= schemas.showUser,)
def register(request:schemas.User, db:Session = Depends(get_db)):
    return authentication.register(request=request , db=db)



@router.post('/login' ,response_model=schemas.Token)
def login(request:OAuth2PasswordRequestForm = Depends(),  db:Session = Depends(get_db)):
   return authentication.login(request=request , db=db)