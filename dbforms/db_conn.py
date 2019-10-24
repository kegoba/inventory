from sqlalchemy import (create_engine, Integer, String,
                Text, DateTime, BigInteger, Column, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


import datetime


import pyodbc
cnxn = pyodbc.connect('Driver={SQL SERVER};'  'server=localhost\SQLEXPRESS;' 'Datebase=INVENTORY;' 'Trusted_connection=yes;')
cursor.execute()



class Student(modelBase):
    __tablename__ = "ITEM_TB"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    staff_name = Column(String)
    item_name = Column(String)
    quantity = Column(Integer)
    description = Column(Text)

