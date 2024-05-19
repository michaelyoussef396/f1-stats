from datetime import datetime
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

    qualify = relationship("Qualify", overlaps="qualify")
    laptimes = relationship("LapTime", back_populates="driver")
    pit_stops = relationship("PitStop", back_populates="driver")


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

    qualify = relationship("Qualify", back_populates="constructor")


class Status(Base):
    __tablename__ = 'status'

    statusId = Column(Integer, primary_key=True)
    status = Column(String(255), nullable=False)


class Race(Base):
    __tablename__ = 'races'
    raceId = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    round = Column(Integer, nullable=False)
    circuitId = Column(Integer, ForeignKey(
        'circuits.circuitId'), nullable=False)
    name = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=True)
    url = Column(String(255), nullable=True)

    circuit = relationship("Circuit", back_populates="races")
    laptimes = relationship("LapTime", back_populates="race")
    qualify = relationship("Qualify")
    pit_stops = relationship("PitStop", back_populates="race")
    qualify = relationship("Qualify", overlaps="qualify")


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


class Qualify(Base):
    __tablename__ = 'qualify'

    qualifyId = Column(Integer, primary_key=True)
    raceId = Column(Integer, ForeignKey('races.raceId'), nullable=True)
    driverId = Column(Integer, ForeignKey('drivers.driverId'), nullable=True)
    constructorId = Column(Integer, ForeignKey(
        'constructors.constructorId'), nullable=True)
    number = Column(Integer, nullable=True)
    position = Column(Integer, nullable=True)

    race = relationship("Race")
    driver = relationship("Driver")
    constructor = relationship("Constructor", back_populates="qualify")


class PitStop(Base):
    __tablename__ = 'pit_stops'

    raceId = Column(Integer, ForeignKey('races.raceId'), primary_key=True)
    driverId = Column(Integer, ForeignKey(
        'drivers.driverId'), primary_key=True)
    stop = Column(Integer, primary_key=True)
    lap = Column(Integer)
    time = Column(Time)
    duration = Column(String(20))
    milliseconds = Column(Integer)

    race = relationship("Race", back_populates="pit_stops")
    driver = relationship("Driver", back_populates="pit_stops")


Base.metadata.create_all(engine)
