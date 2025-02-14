from fastapi import APIRouter
from src.parser_module import parse_json

router: APIRouter = APIRouter()

@router.get("/py")
async def get_json():
    data = parse_json()
    return {"data": data}
