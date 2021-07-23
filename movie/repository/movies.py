import os
from typing import Optional
from fastapi.datastructures import UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.params import File
from sqlalchemy.orm.session import Session
from starlette import status
from starlette.responses import FileResponse
from ..import models, database ,schemas


def get_movies_byId( id , db:Session = Depends(database.get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == id).first()
    if not movie:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f'there is no movie with this id {id}')
    return movie


def get_movies(db:Session = Depends(database.get_db)):
    movies = db.query(models.Movie).all()
    if not movies:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Oops, there is no movies" )
    return movies


def create_movie(request:schemas.Movie , db:Session = Depends(database.get_db)):
   new_movie = models.Movie(title = request.title , description=request.description )
   db.add(new_movie)
   db.commit()
   db.refresh(new_movie)
   return new_movie



def delete_movie( id , db:Session = Depends(database.get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == id).delete(synchronize_session=False)
    db.commit()
    if not movie:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f'there is no movie with this id {id}')
    return {"details" : "Deleted!"}


def update_movie( id , request:schemas.Movie , db:Session = Depends(database.get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == id).update(request)
    db.commit()
    if not movie:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f'there is no movie with this id {id}')
    return {"details" : "Updated!"}


async def uploadImage(image: UploadFile = File(...) , movieId:Optional[int] = None, db:Session = Depends(database.get_db)):
    print(image.file)
    try:
        os.mkdir("images")
    except Exception as e:
        print(e) 
    file_name = image.filename.replace(" ", "-")
    path_name = os.getcwd()+"/images/"+ image.filename.replace(" ", "-") #add date to name
    with open(path_name,'wb+') as f:
        f.write(image.file.read())
        f.close()
    file = jsonable_encoder({"imagePath":path_name})
    add_image(db=db ,movieId=movieId , fileName=file_name)
    return {"filename": path_name}



# to add image to DB
def add_image( fileName , movieId:int ,db:Session):
    update =  db.query(models.Movie).filter(models.Movie.id == movieId).first()
    update.image ="http://127.0.0.1:8000/images/"+fileName
    db.commit()
    db.refresh(update)


def get_image(image_name):
    path_name = "images/"+image_name 
    print(path_name)
    return  FileResponse(path_name)