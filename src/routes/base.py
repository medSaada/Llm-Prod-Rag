from fastapi import FastAPI, APIRouter
from helpers.config import get_settings

#we define the routes here 
router = APIRouter(
    prefix="/api",
    tags=["app_v1"]
)    

@router.get("/")
def root():
    env_settings = get_settings()
    app_name = env_settings.APP_NAME
    app_version = env_settings.APP_VERSION
    return {
        "app_name": app_name,
        "app_version": app_version
        }