from fastapi import APIRouter
import requests
from src.parser_module import parse_csv

SERVER_B_CSV_URL = "http://127.0.0.1:8080/csv/js"

router: APIRouter = APIRouter()

@router.get("/py")
async def get_csv():
    data = parse_csv()
    return {"data": data}

@router.get("/js")
def get_csv_from_js_server():
    response = requests.get(SERVER_B_CSV_URL)
    data = response.json()
    return {"data": data.get("data")}
