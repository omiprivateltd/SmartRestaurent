"""Backend API"""
import json
from fastapi import FastAPI
from fastapi.requests import Request
app = FastAPI()

@app.get("/")
def welcome():
    """Root"""
    return "Status:Online"

@app.post("/addItem")
async def add_new_item(request:Request):
    """Function Used to add new item to database"""
    request_body = await request.body() # getting request body 
    request_body = json.loads(request_body) # from bytes to json 
    