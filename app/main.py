from movie.routers import authentication
from fastapi import FastAPI 
from movie import models
from movie.database import  engine 
from movie.routers import users , movies

app = FastAPI(
    title="Movies Api",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="1.0.0",
)

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(movies.router)
app.include_router(users.router)





