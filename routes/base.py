from fastapi import FastAPI, APIRouter


#we define the routes here 
router = APIRouter()    

@router.get("/")
def root():
    return {"message": "Hello World"}