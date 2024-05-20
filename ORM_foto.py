from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# base for table classes
class Base(DeclarativeBase):
    pass


# sample class mapping table from database
class Album(Base):
    __tablename__ = 'Album'

    # fields and their types
    albumID = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(Integer)
    view = Column(Integer)

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.view = 0


engine = create_engine('mysql+pymysql://root:root@localhost/mydb')

Session = sessionmaker(bind=engine)
session = Session()
album = Album("Dovolená 2024", 10)
session.add(album)
session.commit()
