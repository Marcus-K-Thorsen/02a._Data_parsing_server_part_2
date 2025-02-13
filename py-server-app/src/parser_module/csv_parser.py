import os
import pandas as pd
from src.parser_module.person import Person

CSVPATH = "../../../data/person.csv"

def parse_csv() -> Person | list[Person]:
    __dirname = os.path.dirname(__file__)
    file_path = os.path.join(__dirname, CSVPATH)
    
    csv_data = pd.read_csv(file_path)
    
    persons = []
    for index, row in csv_data.iterrows():
        person_data = {}
        for column in csv_data.columns:
            value = row[column]
            if isinstance(value, str) and ";" in value:
                value_list = [item.strip() if not item.strip().isdigit() else float(item.strip()) for item in value.split(";")]
                person_data[column] = value_list
            elif isinstance(value, (int, float)) or (isinstance(value, str) and value.replace('.', '', 1).isdigit()):
                person_data[column] = float(value)
            else:
                person_data[column] = value.strip() if isinstance(value, str) else value
        persons.append(Person(**person_data, file_type="csv"))
    
    # Uncomment the following line to return a list of Person objects
    # return persons'
    
    # Return a single Person object
    return persons[0]
