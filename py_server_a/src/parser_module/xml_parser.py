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
    if not parsed_person_data and not isinstance(parsed_person_data, dict):
        raise ValueError("No person data found in the XML file.")
    
    person_data = {
        "name": parsed_person_data.get("name", ""),
        "weight": parsed_person_data.get("weight", 0.0),
        "hobbies": parsed_person_data.get("hobbies", {}).get("hobby", [])
    }

    return Person(**person_data, file_type="xml")
