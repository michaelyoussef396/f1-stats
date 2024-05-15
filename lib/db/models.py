from sqlalchemy import Float, create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///f1.db', echo=True)


Base = declarative_base()


class Driver(Base):
    __tablename__ = 'drivers'

    driverId = Column(Integer, primary_key=True)
    driverRef = Column(String)
    number = Column(String)
    code = Column(String)
    forename = Column(String)
    surname = Column(String)
    dob = Column(Date)
    nationality = Column(String)
    url = Column(String)


class Season(Base):
    __tablename__ = 'seasons'

    year = Column(Integer, primary_key=True)
    url = Column(String)


class Circuit(Base):
    __tablename__ = 'circuits'

    circuitId = Column(Integer, primary_key=True)
    circuitRef = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    alt = Column(Integer, nullable=False)
    url = Column(String(255), nullable=True)


class Constructor(Base):
    __tablename__ = 'constructors'

    constructorId = Column(Integer, primary_key=True)
    constructorRef = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    nationality = Column(String(255), nullable=False)
    url = Column(String(255), nullable=True)


class Status(Base):
    __tablename__ = 'status'

    statusId = Column(Integer, primary_key=True)
    status = Column(String(255), nullable=False)


Base.metadata.create_all(engine)
