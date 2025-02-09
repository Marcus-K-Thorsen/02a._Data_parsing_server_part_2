import os
import yaml
from src.parser_module.person import Person

YAMLPATH = "../../../data/person.yaml"

def parse_yaml() -> Person:
    __dirname = os.path.dirname(__file__)
    file_path = os.path.join(__dirname, YAMLPATH)
    
    with open(file_path, "r", encoding="utf-8") as file:
        yaml_text = file.read()

    person_data = yaml.safe_load(yaml_text)

    return Person(**person_data)