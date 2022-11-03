"""Backend API"""
import pyqrcode,png
import json
from fastapi import FastAPI
from fastapi.requests import Request
from database import *
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

file_path = "./images/"
db = Database('test.db')
app = FastAPI()

app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"],allow_credentials=True)
@app.get("/")
def welcome():
    """Root"""
    return "Status:Online"

@app.post("/addItem")
async def add_new_item(request:Request):
    """Function Used to add new item to database"""
    request_body = await request.form() # getting request body 
    print("request body ",request_body)
    item_name=request_body['item_name']
    item_desc=request_body['item_description']
    item_price=request_body['item_price']
    image_data = request_body['image_data']
    file_name = image_data.filename
    with open(file_path+file_name,"wb") as file:
        file.write(await image_data.read())
    # print("name",item_name,"desc",item_desc,"image_price",item_price,"iamge data",image_data)
    # print("data to string",f"{image_data}")
    try:
        db_output = db.insert_item(item_name,item_desc,int(item_price),file_name)
    except Exception as error:
        db_output = error
        print("** exception occured",error)
        return error
    return {"message":db_output}

@app.get("/getItems")
def get_all_item(html:bool=False):
    """Function Used to add new item to database"""
    try:
        raw_html = """<div id="{}" class="text-center">
            <img class='center' src="https://smart-rest.herokuapp.com/Image?image_name={}" height="500" width="500" alt="" style="display:block;margin-left:auto;margin-right: auto;width:50%;">{}</image>
            <h1 class="text-center font-bold"></h1>
        </div>"""
        menu_items = [ ]
        output = db.get_menu()
        for index,item in enumerate(output):
            full_path = f"https://smart-rest.herokuapp.com/Image?image_name={item[4]}"
            item_name=item[1]
            item_price=item[2]
            item_desc=item[3]
            item_image=full_path 
            if html:
                item_desc =  f"{item_name} {item_price} {item_desc}"
                print('item desc',item_desc)
                menu_items.append(raw_html.format("Item"+str(index),item[4],item_desc))
            else:
                menu_items.append([item_name,item_price,item_desc,item_image])
        return menu_items
    except Exception as error:
        output=error
    print("output",output)
    return {"Message":output}

@app.post("/deleteItem")
def delete_item(itemName:str):
    """Function Used to Delete an item from database"""
    try:
       output =  db.execute_command(f"DELETE FROM MENU WHERE ITEMNAME='{itemName}';")
    except Exception as error:
        output = f"Exception While Deleting Item {error}"
    return {"message":output}
    
@app.get("/Image")
def get_image(image_name:str):
    """Function Used to return the image """
    try:
        return FileResponse(path="./images/"+image_name) # not working
    except RuntimeError as error:
        return error

@app.get("/getQR")
def get_qr():
    """Function Used to Generate New QR"""
    url=pyqrcode.create("https://smart-rest-front-end.herokuapp.com/items.html")
    url.png("QR.png",scale=6)
    return FileResponse("QR.png")

if __name__=="__main__":
    print(get_qr())
