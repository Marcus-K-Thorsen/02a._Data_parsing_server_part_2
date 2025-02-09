import os
import json
from src.parser_module.person import Person

JSONPATH = "../../../data/person.json"

def parse_json() -> Person:
    __dirname = os.path.dirname(__file__)
    file_path = os.path.join(__dirname, JSONPATH)
    
    with open(file_path, "r", encoding="utf-8") as file:
        json_text = file.read()

    person_data = json.loads(json_text)

    return Person(**person_data)