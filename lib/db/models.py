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
    results = relationship("Result", back_populates="driver")

    def _init__(self, driverId, driverRef, number, code, forename, surname, dob, nationality, url):
        self.driverId = driverId
        self.driverRef = driverRef
        self.number = number
        self.code = code
        self.forename = forename
        self.surname = surname
        self.dob = dob
        self.nationality = nationality
        self.url = url

    def __repr__(self):
        return f"<Driver(driverId={self.driverId}, driverRef={self.driverRef}, number={self.number}, code={self.number}, forename={self.forename}, surname={self.surname}, dob={self.dob}, nationality={self.nationality}, url={self.url} )>"


class Season(Base):
    __tablename__ = 'seasons'

    year = Column(Integer, primary_key=True)
    url = Column(String)

    def __init__(self, year, url):
        self.year = year
        self.url = url

    def __repr__(self):
        return f"<Season(year={self.year}, url={self.url})>"


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

    def __init__(self, circuitId, circuitRef, name, location, country, lat, lng, alt, url):
        self.circuitId = circuitId
        self.circuitRef = circuitRef
        self.name = name
        self.location = location
        self.country = country
        self.lat = lat
        self.lng = lng
        self.alt = alt
        self.url = url

    def __repr__(self):
        return f"<Circuit(circuitId={self.circuitId}, circuitRef={self.circuitRef}, name={self.name}, location={self.location}, country={self.country}, lat={self.lat}, lng={self.lng}, alt={self.alt}, url={self.url} )>"


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
    results = relationship("Result", back_populates="constructor")

    def __init__(self, constructorId, constructorRef, name, nationality, url):
        self.constructorId = constructorId
        self.constructorRef = constructorRef
        self.name = name
        self.nationality = nationality
        self.url = url

    def __repr__(self):
        return f"<Constructor(constructorId={self.constructorId}, constructorRef={self.constructorRef}, name={self.name}, nationality={self.nationality}, url={self.url})>"


class Status(Base):
    __tablename__ = 'status'

    statusId = Column(Integer, primary_key=True)
    status = Column(String(255), nullable=False)

    def __init__(self, statusId, status):
        self.statusId = statusId
        self.status = status

    def __repr__(self):
        return f"<Status(statusId={self.statusId}, status={self.status})>"


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
    driver_standings = relationship("DriverStanding", back_populates="race")
    constructor_standings = relationship(
        "ConstructorStanding", back_populates="race")
    constructor_results = relationship(
        "ConstructorResult", back_populates="race")
    sprint_results = relationship("SprintResult", back_populates="race")
    results = relationship("Result", back_populates="race")

    def __init__(self, raceId, year, round, circuitId, name, date, time, url):
        self.raceId = raceId
        self.year = year
        self.round = round
        self.circuitId = circuitId
        self.name = name
        self.date = date
        self.time = time
        self.url = url

    def __repr__(self):
        return f"<Race(raceId={self.raceId}, year={self.year}, round={self.round}, circuitId={self.circuitId}, name={self.name}, date={self.date}, time={self.time}, url={self.url} )>"


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

    def _init__(self, raceId, driverId, lap, position, time, milliseconds):
        self.raceId = raceId
        self.driverId = driverId
        self.lap = lap
        self.position = position
        self.time = time
        self.milliseconds = milliseconds

    def __repr__(self):
        return f"<LapTime(raceId={self.raceId}, driverId={self.driverId}, lap={self.lap}, position={self.position}, time={self.time}, milliseconds={self.milliseconds})>"


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

    def __init__(self, qualifyId, raceId, driverId, constructorId, number, position):
        self.qualifyId = qualifyId
        self.raceId = raceId
        self.driverId = driverId
        self.constructorId = constructorId
        self.number = number
        self.position = position

    def __repr__(self):
        return f"<Qualify(qualifyId={self.qualifyId}, raceId={self.raceId}, driverId={self.driverId}, constructorId={self.constructorId}, number={self.number}, position={self.position} )>"


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

    def __init__(self, raceId, driverId, stop, lap, time, duraction, milliseconds):
        self.raceId = raceId
        self.driverId = driverId
        self.stop = stop
        self.lap = lap
        self.time = time
        self.duration = duraction
        self.milliseconds = milliseconds

    def __repr__(self):
        return f"<PitStop(raceId={self.raceId}, driverId={self.driverId}, stop={self.stop}, lap={self.lap}, time={self.time}, duration={self.duration}, milliseconds={self.milliseconds})>"


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

    def __init__(self, driverStandingsId, raceId, driverId, points, position, posiitionText, wins):
        self.driverStandingsId = driverStandingsId
        self.raceId = raceId
        self.driverId = driverId
        self.points = points
        self.position = position
        self.positionText = posiitionText
        self.wins = wins


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

    def __init__(self, constructorStandingsId, raceId, constructorId, points, position, positionText, wins):
        self.constructorStandingsId = constructorStandingsId
        self.raceId = raceId
        self.constructorId = constructorId
        self.points = points
        self.position = position
        self.positionText = positionText
        self.wins = wins

    def __repr__(self):
        return f"<ConstructorStanding(constructorStandingsId={self.constructorStandingsId}, raceId={self.raceId}, constructorId={self.constructorId}, points={self.points}, position={self.position}, positionText={self.positionText}, wins={self.wins})>"


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

    def __init__(self, constructorResultsId, raceId, constructorId, points, status):
        self.constructorResultsId = constructorResultsId
        self.raceId = raceId
        self.constructorId = constructorId
        self.points = points
        self.status = status

    def __repr__(self):
        return f"<ConstructorResult(constructorResultsId={self.constructorResultsId}, raceId={self.raceId}, constructorId={self.constructorId}, points={self.points}, status={self.status})>"


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

    def __init__(self, resultId, raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points, laps, time, milliseconds, fastestLap, fastestLapTime, statusId):
        self.resultId = resultId
        self.raceId = raceId
        self.driverId = driverId
        self.constructorId = constructorId
        self.number = number
        self.grid = grid
        self.position = position
        self.positionText = positionText
        self.positionOrder = positionOrder
        self.points = points
        self.laps = laps
        self.time = time
        self.milliseconds = milliseconds
        self.fastestLap = fastestLap
        self.fastestLapTime = fastestLapTime
        self.statusId = statusId

    def __repr__(self):
        return f"<SprintResult(resultId={self.resultId}, raceId={self.raceId}, driverId={self.driverId}, constructorId={self.constructorId}, number={self.number}, grid={self.grid}, position={self.position}, positionText={self.positionText}, positionOrder={self.positionOrder}, points={self.points}, laps={self.laps}, time={self.time}, milliseconds={self.milliseconds}, fastestLap={self.fastestLap}, fastestLapTime={self.fastestLapTime}, statusId={self.status} )>"


class Result(Base):
    __tablename__ = 'results'

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
    rank = Column(Integer)
    fastestLapTime = Column(String(255))
    fastestLapSpeed = Column(String(255))
    statusId = Column(Integer, ForeignKey('status.statusId'))

    race = relationship("Race", back_populates="results")
    driver = relationship("Driver", back_populates="results")
    constructor = relationship("Constructor", back_populates="results")
    status = relationship("Status")

    def __init__(self, resultId, raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points, laps, time, milliseconds, fastestLap, rank, fastestLapTime, fastestLapSpeed, statusId):
        self.resultId = resultId
        self.raceId = raceId
        self.driverId = driverId
        self.constructorId = constructorId
        self.number = number
        self.grid = grid
        self.position = position
        self.positionText = positionText
        self.positionOrder = positionOrder
        self.points = points
        self.laps = laps
        self.time = time
        self.milliseconds = milliseconds
        self.fastestLap = fastestLap
        self.rank = rank
        self.fastestLapTime = fastestLapTime
        self.fastestLapSpeed = fastestLapSpeed
        self.statusId = statusId

    def __repr__(self):
        return f"<Result(resultId={self.resultId}, raceId={self.raceId}, driverId={self.driverId}, constructorId={self.constructorId}, number={self.number}, grid={self.grid}, position={self.position}, positionText={self.positionText}, positionOrder={self.positionOrder}, points={self.points}, laps={self.laps}, time={self.time}, milliseconds={self.milliseconds}, fastestLap={self.fastestLap}, rank={self.rank}, fastestLapTime={self.fastestLapTime}, fastestLapSpeed={self.fastestLapSpeed}, statusId={self.statusId} )>"


Base.metadata.create_all(engine)
