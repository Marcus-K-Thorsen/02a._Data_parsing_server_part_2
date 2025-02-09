from fastapi import APIRouter
from src.parser_module import parse_xml

router: APIRouter = APIRouter()

@router.get("/xml")
async def get_xml():
    data = parse_xml()
    return {"data": data}
