import os
import csv
from sqlalchemy.orm import sessionmaker
from models import Status, engine


Session = sessionmaker(bind=engine)


def get_csv(csv_name):
    return f"csv/{csv_name}"


def seed_tables(table_name, model):
    csv_file_path = get_csv(table_name)

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


table_name = "status.csv"
model = Status

seed_tables(table_name, model)
