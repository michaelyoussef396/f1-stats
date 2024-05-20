import os
import csv
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import Result, Race, engine, Status, Season, Driver, Constructor, Circuit, LapTime, Qualify, PitStop, DriverStanding, ConstructorStanding, ConstructorResult, SprintResult

Session = sessionmaker(bind=engine)

table = "results.csv"
model = Result


def get_csv(csv_name):
    return f"csv/{csv_name}"


def seed_races(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            raceId = int(row['raceId'])
            year = int(row['year'])
            round = int(row['round'])
            circuitId = int(row['circuitId'])
            name = row['name']
            date_str = row['date']
            date = datetime.strptime(date_str, '%d/%m/%Y').date()
            time_str = row['time']
            time = datetime.strptime(
                time_str, '%H:%M:%S').time() if time_str != '\\N' else None
            url = row['url']

            instance = model(
                raceId=raceId,
                year=year,
                round=round,
                circuitId=circuitId,
                name=name,
                date=date,
                time=time,
                url=url
            )
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


def seed_status(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            statusId = int(row['statusId']),
            status = row['status']

            instance = model(**row)
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


def seed_constructors(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            constructorId = int(row['constructorId']),
            constructorRef = row['constructorRef'],
            name = row['name'],
            nationality = row['nationality'],
            url = row['url']

            instance = model(**row)
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


def seed_circuits(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            circuitId = int(row['circuitId']),
            circuitRef = row['circuitRef'],
            name = row['name'],
            location = row['location'],
            country = row['country'],
            lat = float(row['lat']),
            lng = float(row['lng']),
            alt = int(row['alt']),
            url = row['url']

            instance = model(**row)
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


def seed_seasons(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            row['year'] = int(row['year'])
            url = row['url']

            instance = model(**row)
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


def seed_drivers(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            driverId = int(row['driverId']),
            driverRef = row['driverRef'],
            number = row['number'],
            code = row['code'],
            forename = row['forename'],
            surname = row['surname'],
            # Convert to date object
            dob = datetime.strptime(row['dob'], '%Y-%m-%d').date(),
            nationality = row['nationality'],
            url = row['url']

            instance = model(**row)
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


def seed_lapTime(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            raceId = int(row['raceId'])
            driverId = int(row['driverId'])
            lap = int(row['lap'])
            position = int(row['position'])
            time_str = row['time']
            time = time_str.split(':')
            milliseconds_parts = int(
                time[0]) * 60000 + int(time[1].replace('.', '')) * 1000
            milliseconds = milliseconds_parts

            instance = model(**row)
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


def seed_qualify(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            qualifyId = int(row['qualifyId'])
            raceId = int(row['raceId']) if row['raceId'] else None
            driverId = int(row['driverId']) if row['driverId'] else None
            constructorId = int(row['constructorId']
                                ) if row['constructorId'] else None
            number = int(row['number']) if row['number'] else None
            position = int(row['position']) if row['position'] else None

            instance = model(**row)
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


def seed_pit_stop(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            raceId = int(row['raceId'])
            driverId = int(row['driverId'])
            stop = int(row['stop'])
            lap = int(row['lap'])
            time_str = row['time']
            time = datetime.strptime(time_str, '%H:%M:%S').time()
            duration = row['duration']
            milliseconds = int(row['milliseconds'])

            instance = model(
                raceId=raceId,
                driverId=driverId,
                stop=stop,
                lap=lap,
                time=time,
                duration=duration,
                milliseconds=milliseconds
            )
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


def seed_driver_standing(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            driverStandingsId = int(row['driverStandingsId'])
            raceId = int(row['raceId'])
            driverId = int(row['driverId'])
            points = float(row['points'])
            position = int(row['position'])
            positionText = row['positionText']
            wins = int(row['wins'])

            instance = model(
                driverStandingsId=driverStandingsId,
                raceId=raceId,
                driverId=driverId,
                points=points,
                position=position,
                positionText=positionText,
                wins=wins
            )
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


def seed_constructor_standings(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            constructorStandingsId = int(row['constructorStandingsId'])
            raceId = int(row['raceId'])
            constructorId = int(row['constructorId'])
            points = float(row['points'])
            position = int(row['position'])
            positionText = row['positionText']
            wins = int(row['wins'])

            instance = model(
                constructorStandingsId=constructorStandingsId,
                raceId=raceId,
                constructorId=constructorId,
                points=points,
                position=position,
                positionText=positionText,
                wins=wins
            )
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


def seed_constructor_results(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            constructorResultsId = int(row['constructorResultsId'])
            raceId = int(row['raceId'])
            constructorId = int(row['constructorId'])
            points = float(row['points'])
            status = row['status'] if row['status'] != '\\N' else None

            instance = model(
                constructorResultsId=constructorResultsId,
                raceId=raceId,
                constructorId=constructorId,
                points=points,
                status=status
            )
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


def seed_sprint_results(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            resultId = int(row['resultId'])
            raceId = int(row['raceId'])
            driverId = int(row['driverId'])
            constructorId = int(row['constructorId'])
            number = int(row['number']) if row['number'] != '\\N' else None
            grid = int(row['grid']) if row['grid'] != '\\N' else None
            position = int(
                row['position']) if row['position'] != '\\N' else None
            positionText = row['positionText'] if row['positionText'] != '\\N' else None
            positionOrder = int(
                row['positionOrder']) if row['positionOrder'] != '\\N' else None
            points = float(row['points']) if row['points'] != '\\N' else None
            laps = int(row['laps']) if row['laps'] != '\\N' else None
            time = row['time'] if row['time'] != '\\N' else None
            milliseconds = int(row['milliseconds']
                               ) if row['milliseconds'] != '\\N' else None
            fastestLap = int(row['fastestLap']
                             ) if row['fastestLap'] != '\\N' else None
            fastestLapTime = row['fastestLapTime'] if row['fastestLapTime'] != '\\N' else None
            statusId = int(
                row['statusId']) if row['statusId'] != '\\N' else None

            instance = model(
                resultId=resultId,
                raceId=raceId,
                driverId=driverId,
                constructorId=constructorId,
                number=number,
                grid=grid,
                position=position,
                positionText=positionText,
                positionOrder=positionOrder,
                points=points,
                laps=laps,
                time=time,
                milliseconds=milliseconds,
                fastestLap=fastestLap,
                fastestLapTime=fastestLapTime,
                statusId=statusId
            )
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


def seed_results(table, model):
    csv_file_path = get_csv(table)
    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)
        data = []
        for row in csv_data:
            resultId = int(row['resultId'])
            raceId = int(row['raceId'])
            driverId = int(row['driverId'])
            constructorId = int(row['constructorId'])
            number = int(row['number']) if row['number'] != '\\N' else None
            grid = int(row['grid']) if row['grid'] != '\\N' else None
            position = int(
                row['position']) if row['position'] != '\\N' else None
            positionText = row['positionText'] if row['positionText'] != '\\N' else None
            positionOrder = int(
                row['positionOrder']) if row['positionOrder'] != '\\N' else None
            points = float(row['points']) if row['points'] != '\\N' else None
            laps = int(row['laps']) if row['laps'] != '\\N' else None
            time = row['time'] if row['time'] != '\\N' else None
            milliseconds = int(row['milliseconds']
                               ) if row['milliseconds'] != '\\N' else None
            fastestLap = int(row['fastestLap']
                             ) if row['fastestLap'] != '\\N' else None
            rank = int(row['rank']) if row['rank'] != '\\N' else None
            fastestLapTime = row['fastestLapTime'] if row['fastestLapTime'] != '\\N' else None
            fastestLapSpeed = row['fastestLapSpeed'] if row['fastestLapSpeed'] != '\\N' else None
            statusId = int(
                row['statusId']) if row['statusId'] != '\\N' else None

            instance = model(
                resultId=resultId,
                raceId=raceId,
                driverId=driverId,
                constructorId=constructorId,
                number=number,
                grid=grid,
                position=position,
                positionText=positionText,
                positionOrder=positionOrder,
                points=points,
                laps=laps,
                time=time,
                milliseconds=milliseconds,
                fastestLap=fastestLap,
                rank=rank,
                fastestLapTime=fastestLapTime,
                fastestLapSpeed=fastestLapSpeed,
                statusId=statusId
            )
            data.append(instance)

    session = Session()
    session.add_all(data)
    session.commit()
    session.close()


seed_sprint_results(table, model)
