import os
import csv
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import Driver, engine

Session = sessionmaker(bind=engine)
csv_file_path = "csv/drivers.csv"

with open(csv_file_path, 'r') as file:
    csv_data = csv.DictReader(file)

    # Convert the data to a list and process the 'dob' values
    data = []
    for row in csv_data:
        row['dob'] = datetime.strptime(row['dob'], '%Y-%m-%d').date()
        data.append(row)

    session = Session()
    session.bulk_insert_mappings(Driver, data)
    session.commit()
    session.close()
