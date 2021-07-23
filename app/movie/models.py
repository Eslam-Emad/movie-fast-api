from sqlalchemy import  Column, Integer, String
from movie.database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description= Column(String)
    image= Column(String)
    #release_date= Column(DateTime)
    #star= Column(String)
    #language= Column(String) EN - AR
    #category= Column(String)
    #status= Column(String) RA TR RC(Recomended)


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email= Column(String)
    password= Column(String)
    #authority = Column(String)     ( Admin - User )
   