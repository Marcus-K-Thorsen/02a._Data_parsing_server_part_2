from fastapi import APIRouter
from src.parser_module import parse_yaml

router: APIRouter = APIRouter()

@router.get("/yaml")
async def get_yaml():
    data = parse_yaml()
    return {"data": data}
