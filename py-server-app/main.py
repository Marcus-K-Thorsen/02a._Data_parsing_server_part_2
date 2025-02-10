from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.endpoints import (
    csv_router, 
    json_router, 
    text_router,
    xml_router, 
    yaml_router
    )

app = FastAPI()

CORS_SETTINGS = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"]
}

app.add_middleware(CORSMiddleware, **CORS_SETTINGS)


app.include_router(csv_router, prefix='/py')
app.include_router(json_router, prefix='/py')
app.include_router(text_router, prefix='/py')
app.include_router(xml_router, prefix='/py')
app.include_router(yaml_router, prefix='/py')


@app.get("/py")
def read_root():
    return { "data": "Root Python Route" }
