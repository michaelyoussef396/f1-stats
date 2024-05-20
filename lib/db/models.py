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
    driver_standings = relationship("DriverStanding", back_populates="driver")
    sprint_results = relationship("SprintResult", back_populates="driver")


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
    constructor_standings = relationship(
        "ConstructorStanding", back_populates="constructor")
    constructor_results = relationship(
        "ConstructorResult", back_populates="constructor")

    sprint_results = relationship("SprintResult", back_populates="constructor")


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
    driver_standings = relationship("DriverStanding", back_populates="race")
    constructor_standings = relationship(
        "ConstructorStanding", back_populates="race")
    constructor_results = relationship(
        "ConstructorResult", back_populates="race")
    sprint_results = relationship("SprintResult", back_populates="race")


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


class DriverStanding(Base):
    __tablename__ = 'driver_standings'

    driverStandingsId = Column(Integer, primary_key=True)
    raceId = Column(Integer, ForeignKey('races.raceId'), nullable=False)
    driverId = Column(Integer, ForeignKey('drivers.driverId'), nullable=False)
    points = Column(Float, nullable=False)
    position = Column(Integer, nullable=False)
    positionText = Column(String(255), nullable=False)
    wins = Column(Integer, nullable=False)

    race = relationship("Race", back_populates="driver_standings")
    driver = relationship("Driver", back_populates="driver_standings")


class ConstructorStanding(Base):
    __tablename__ = 'constructor_standings'

    constructorStandingsId = Column(Integer, primary_key=True)
    raceId = Column(Integer, ForeignKey('races.raceId'), nullable=False)
    constructorId = Column(Integer, ForeignKey(
        'constructors.constructorId'), nullable=False)
    points = Column(Float, nullable=False)
    position = Column(Integer, nullable=False)
    positionText = Column(String(255), nullable=False)
    wins = Column(Integer, nullable=False)

    race = relationship("Race", back_populates="constructor_standings")
    constructor = relationship(
        "Constructor", back_populates="constructor_standings")


class ConstructorResult(Base):
    __tablename__ = 'constructor_results'

    constructorResultsId = Column(Integer, primary_key=True)
    raceId = Column(Integer, ForeignKey('races.raceId'), nullable=False)
    constructorId = Column(Integer, ForeignKey(
        'constructors.constructorId'), nullable=False)
    points = Column(Float, nullable=False)
    status = Column(String(255))

    race = relationship("Race", back_populates="constructor_results")
    constructor = relationship(
        "Constructor", back_populates="constructor_results")


class SprintResult(Base):
    __tablename__ = 'sprint_results'

    resultId = Column(Integer, primary_key=True)
    raceId = Column(Integer, ForeignKey('races.raceId'), nullable=False)
    driverId = Column(Integer, ForeignKey('drivers.driverId'), nullable=False)
    constructorId = Column(Integer, ForeignKey(
        'constructors.constructorId'), nullable=False)
    number = Column(Integer)
    grid = Column(Integer)
    position = Column(Integer)
    positionText = Column(String(255))
    positionOrder = Column(Integer)
    points = Column(Float)
    laps = Column(Integer)
    time = Column(String(255))
    milliseconds = Column(Integer)
    fastestLap = Column(Integer)
    fastestLapTime = Column(String(255))
    statusId = Column(Integer, ForeignKey('status.statusId'))

    race = relationship("Race", back_populates="sprint_results")
    driver = relationship("Driver", back_populates="sprint_results")
    constructor = relationship("Constructor", back_populates="sprint_results")
    status = relationship("Status")


Base.metadata.create_all(engine)
