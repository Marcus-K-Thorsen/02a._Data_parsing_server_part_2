from fastapi import APIRouter
import requests
from src.parser_module import parse_txt

SERVER_B_TXT_URL = "http://127.0.0.1:8080/txt/js"

router: APIRouter = APIRouter()

@router.get("/py")
async def get_txt():
    data = parse_txt()
    return {"data": data}

@router.get("/js")
def get_txt_from_js_server():
    response = requests.get(SERVER_B_TXT_URL)
    data = response.json()
    return {"data": data.get("data")}
