import os
import xmltodict
from src.parser_module.person import Person

XMLPATH = "../../../data/person.xml"

def parse_xml() -> Person:
    __dirname = os.path.dirname(__file__)
    file_path = os.path.join(__dirname, XMLPATH)
    
    with open(file_path, "r", encoding="utf-8") as file:
        xml_text = file.read()

    parsed_person_data = xmltodict.parse(xml_text)["person"]
    person_data = {}

    for key, value in parsed_person_data.items():
        if key == "hobbies":
            person_data[key] = [item.strip() for item in value["hobby"]]
        elif isinstance(value, str) and value.replace('.', '', 1).isdigit():
            person_data[key] = float(value)
        else:
            person_data[key] = value

    return Person(**person_data, file_type="xml")
