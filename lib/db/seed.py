import os
import csv
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import Race, engine

Session = sessionmaker(bind=engine)


def get_csv(csv_name):
    return f"csv/{csv_name}"


def seed_tables(table_name, model):
    csv_file_path = get_csv(table_name)
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


table_name = "races.csv"
model = Race
seed_tables(table_name, model)
