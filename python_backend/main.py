"""Backend API"""
import json
from fastapi import FastAPI
from fastapi.requests import Request
from database import Database

db = Database('test.db')
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
    try:
        db_output = db.insert_item(request_body['item_name'],request_body["item_desc"],request_body["item_price"],request_body["item_image"])
    except Exception as error:
        db_output = error
    return {"message":db_output}

@app.get("/getItems")
def get_all_item():
    """Function Used to add new item to database"""
    try:
        output = db.get_menu()
    except Exception as error:
        output=error
    print("output",output)
    return {"Message":output}

print(get_all_item())

