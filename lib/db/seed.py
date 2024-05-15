import os
import csv
from sqlalchemy.orm import sessionmaker
from models import Circuit, engine


Session = sessionmaker(bind=engine)


def get_csv(csv_name):
    return f"csv/{csv_name}"


def seed_tables(table_name, model):
    csv_file_path = get_csv(table_name)

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


table_name = "circuits.csv"
model = Circuit

seed_tables(table_name, model)
