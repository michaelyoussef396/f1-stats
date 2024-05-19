import os
import csv
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import Race, engine, Status, Season, Driver, Constructor, Circuit, LapTime

Session = sessionmaker(bind=engine)

table = "lap_times.csv"
model = LapTime


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


seed_lapTime(table, model)
