from movie.oauth2 import get_current_user
from typing import List, Optional
from fastapi import APIRouter ,Depends
from fastapi.datastructures import UploadFile
from fastapi.params import File
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import user
from starlette import status
from .. import schemas , database
from ..repository import  movies


router = APIRouter(tags=['Movies'] , prefix="/movies")


@router.get("/{id}" , status_code=status.HTTP_200_OK, response_model=schemas.showMovie)
def get_movies_byId(
    id,
    db:Session = Depends(database.get_db),
    current_user:schemas.User = Depends(get_current_user)
    ):
    return movies.get_movies_byId(id=id , db=db)



@router.get("/" , status_code=200 , response_model=List[schemas.showMovie] )
def get_movies(
    db:Session = Depends(database.get_db) ,
 ):
    return movies.get_movies(db=db)



@router.post("/" , status_code=status.HTTP_201_CREATED)
def create_movie(
    request:schemas.Movie,
     db:Session = Depends(database.get_db),
     current_user:schemas.User = Depends(get_current_user)
     ):
   return movies.create_movie(request=request, db=db)



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie( 
    id, 
    db:Session = Depends(database.get_db) ,
    current_user:schemas.User = Depends(get_current_user)
    ):
   return movies.delete_movie(id=id, db=db)




@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_movie(
    id,
    request:schemas.Movie,
     db:Session = Depends(database.get_db),
     current_user:schemas.User = Depends(get_current_user)
      ):
   return movies.update_movie(id=id,request=request, db=db)





@router.post("/upload_poster/", status_code=status.HTTP_202_ACCEPTED)
async def uploadImage(
    image: UploadFile = File(...),
    movieId:Optional[int] = None,
    db:Session = Depends(database.get_db), 
    current_user:schemas.User = Depends(get_current_user)
      ):
    return movies.uploadImage(image=image, movieId=movieId, db=db)



# show poster whene brows
@router.get('/images/{image_name}')
def get_image(image_name):
    path_name = "images/"+image_name   
    return  movies.get_image(image_name=image_name)