import os
import csv
from sqlalchemy.orm import sessionmaker
from models import Constructor, engine


Session = sessionmaker(bind=engine)


def get_csv(csv_name):
    return f"csv/{csv_name}"


def seed_tables(table_name, model):
    csv_file_path = get_csv(table_name)

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


table_name = "constructors.csv"
model = Constructor

seed_tables(table_name, model)
