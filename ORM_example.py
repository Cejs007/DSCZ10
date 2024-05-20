from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# base for table classes
class Base(DeclarativeBase):
    pass


# sample class mapping table from database
class Client(Base):
    __tablename__ = 'clients'

    # fields and their types
    client_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    city = Column(String)

    def __init__(self, first_name, last_name, address, city):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city


engine = create_engine('mysql+pymysql://root:root@localhost/car_rental')

Session = sessionmaker(bind=engine)
session = Session()
client_1 = Client('Michal', 'Maliszewski', 'nejaka', 'Terlicko')
session.add(client_1)
session.commit()

#client_2 = Client("Arnold", "Schwarzeneger", "VIP", "LA")
#session.add(client_2)
#session.commit()
