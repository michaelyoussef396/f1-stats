import os
import csv
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import Driver, engine
from helpers import get_csv
Session = sessionmaker(bind=engine)


"drivers.csv"


def seed_tables(table_name, model):
    csv_file_path = get_csv(table_name)

    with open(csv_file_path, 'r') as file:
        csv_data = csv.DictReader(file)

        # Convert the data to a list and process the 'dob' values
        data = []
        for row in csv_data:
            instance = model(**row)
            data.append(instance)

        session = Session()
        session.bulk_insert_mappings(Driver, data)
        session.commit()
        session.close()
