#This file is for setting up database tables as an models
from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import null
from pydantic import*

class Iproject(Base):
    __tablename__ = "iproject_items" # Table name
    # Columns contain by table
    item_id = Column(Integer, primary_key=True,nullable=False)
    item_name = Column(String, nullable=False)
    item_price = Column(Integer, nullable=False)
    item_quantity = Column(Integer, nullable=False)