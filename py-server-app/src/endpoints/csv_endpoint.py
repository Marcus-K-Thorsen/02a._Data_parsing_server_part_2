from fastapi import APIRouter
from src.parser_module import parse_csv

router: APIRouter = APIRouter()

@router.get("/csv")
async def get_csv():
    data = parse_csv()
    return {"data": data}
