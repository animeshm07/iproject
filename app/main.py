#for master only
from . import models
from fastapi import *
from .schema import Items
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .database import engine, get_db
from app import models


#Create the database tables¶ https://fastapi.tiangolo.com/tutorial/sql-databases/
models.Base.metadata.create_all(bind=engine)

# Step 1 create object fof fastapi
app = FastAPI() 

# This endppoint is created using FASTAPI 
@app.get("/")
def openApp():
    return {"Details":"App is is running..."}

@app.post("/create_item")
def create_item(post:Items, db: Session = Depends(get_db)):
    item_added = models.Iproject(item_name=post.item_name,
                            item_price=post.item_price,
                            item_quantity=post.item_quantity)
    db.add(item_added)
    db.commit()
    db.refresh(item_added)
    return item_added
    
# THis is for retriving all items 
@app.get("/items/")
def get_all_items(db: Session = Depends(get_db)):
    all_items = db.query(models.Iproject).all()
    return all_items
    
# THis is for retriving items by id
@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    return {"item_id": item_id}

#This is taking the data from url as put and adding them into the parameters 
# This is update methods
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Items):
    return {"item_name": item.item_name, "Item_Quantity":item.item_quantity, "Item_Price": item.item_price, "item_id": item_id}


