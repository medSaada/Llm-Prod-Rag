from fastapi import FastAPI, APIRouter
import os

#we define the routes here 
router = APIRouter(
    prefix="/api",
    tags=["app_v1"]
)    

@router.get("/")
def root():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "app_name": app_name,
        "app_version": app_version
        }