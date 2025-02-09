import os
from src.parser_module.person import Person

TEXTPATH = "../../../data/person.txt"

def parse_txt() -> Person:
    __dirname = os.path.dirname(__file__)
    file_path = os.path.join(__dirname, TEXTPATH)
    
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    variables = text.split("\n")

    person_data = {}

    for variable in variables:
        data = variable.split("=")
        data_key = data[0].strip()
        data_value = data[1].strip()
        
        if data_value.startswith(':'):
            data_value_list = data_value[1:].split(",")
            data_value_list = [value.strip() if not value.strip().isdigit() else float(value.strip()) for value in data_value_list]
            data_value = data_value_list
        elif data_value.isdigit():
            data_value = float(data_value)
        
        person_data[data_key] = data_value

    return Person(**person_data)
