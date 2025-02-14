from fastapi import APIRouter
import requests
from src.parser_module import parse_json

SERVER_B_JSON_URL = "http://127.0.0.1:8080/json/js"

router: APIRouter = APIRouter()

@router.get("/py")
async def get_json():
    data = parse_json()
    return {"data": data}



@router.get("/js")
def get_json_from_js_server():
    response = requests.get(SERVER_B_JSON_URL)
    data = response.json()
    return {"data": data.get("data")}
