from fastapi import APIRouter
import requests
from src.parser_module import parse_xml

SERVER_B_XML_URL = "http://127.0.0.1:8080/xml/js"

router: APIRouter = APIRouter()

@router.get("/py")
async def get_xml():
    data = parse_xml()
    return {"data": data}

@router.get("/js")
def get_xml_from_js_server():
    response = requests.get(SERVER_B_XML_URL)
    data = response.json()
    return {"data": data.get("data")}
