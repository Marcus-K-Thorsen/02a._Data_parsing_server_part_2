from fastapi import APIRouter
from src.parser_module import parse_txt

router: APIRouter = APIRouter()

@router.get("/py")
async def get_txt():
    data = parse_txt()
    return {"data": data}
