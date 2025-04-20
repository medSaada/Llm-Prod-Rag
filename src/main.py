from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()#load the environment variables in the system make sure to call it before importing the routes
from routes import base
app = FastAPI()
app.include_router(base.router)