from fastapi import APIRouter
import requests
from src.parser_module import parse_yaml

SERVER_B_YAML_URL = "http://127.0.0.1:8080/yaml/js"

router: APIRouter = APIRouter()

@router.get("/py")
async def get_yaml():
    data = parse_yaml()
    return {"data": data}

@router.get("/js")
def get_yaml_from_js_server():
    response = requests.get(SERVER_B_YAML_URL)
    data = response.json()
    return {"data": data.get("data")}
