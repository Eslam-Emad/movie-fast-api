from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic.networks import HttpUrl
from sqlalchemy.sql.sqltypes import DateTime



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class Movie(BaseModel):
    title:str
    description:str
    image:str
    #release_date:datetime.datetime
    #star:str 
    #language:str 
    #category:str
    #status:str

class showMovie(Movie):
    id:int
    
    class Config:
        orm_mode = True



class User(BaseModel):
    name:str
    email:str
    password:str
    #authority:str


class showUser(BaseModel):
    id:int
    name:str
    email:str
    #authority:str


    class Config:
        orm_mode = True


class Login(BaseModel):
    email:str
    password:str