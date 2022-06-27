# This file is for storing all the schemas or types for api request body

from pydantic import BaseModel

class Items(BaseModel):
    item_name : str
    item_quantity : int
    item_price : float
    # item_id: int