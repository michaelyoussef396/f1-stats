from sqlalchemy import Float, ForeignKey, Time, create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


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

    laptimes = relationship("LapTime", back_populates="driver")


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

    races = relationship("Race", back_populates="circuit")


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


class Race(Base):
    __tablename__ = 'races'
    raceId = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    round = Column(Integer, nullable=False)
    circuitId = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=True)
    url = Column(String(255), nullable=True)

    circuit = relationship("Circuit", back_populates="races")
    laptimes = relationship("LapTime", back_populates="race")


class LapTime(Base):
    __tablename__ = 'laptimes'

    raceId = Column(Integer, ForeignKey('races.raceId'), primary_key=True)
    driverId = Column(Integer, ForeignKey(
        'drivers.driverId'), primary_key=True)
    lap = Column(Integer, primary_key=True)
    position = Column(Integer)
    time = Column(String(255))
    milliseconds = Column(Integer)

    race = relationship("Race", back_populates="laptimes")
    driver = relationship("Driver", back_populates="laptimes")


Base.metadata.create_all(engine)
