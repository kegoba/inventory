"""
Sample script to create tables using sqlalchemy ORM

sqlalchemy documentation link ==>
    http://docs.sqlalchemy.org/en/latest/orm/tutorial.html

"""
from sqlalchemy import (create_engine, Integer, String,
                Text, DateTime, BigInteger, Column, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
#import psycopg2


import datetime

# +-------------------------+-------------------------+
# +-------------------------+-------------------------+
#postgreSQL3W
# mssql+pyodbc://scott:tiger@myhost:port/databasename?driver=SQL+Server+Native+Client+10.0
#db_schema = create_engine("mssql+pyodbc://@TestDNA", echo=True)
#db_schema = create_engine("postgres://progres:kelvine@localhost:5432/inventory?",echo=True)
#psycopg2.connect(db)
#modelBase = declarative_base()
#conn_str = "mssql+pyodbc://SA:$5y5db4123@127.0.0.1:1433/TestDB?driver=ODBC+Driver+17+for+SQL+Server"
#db_schema = create_engine(conn_str, echo=True)
#db_schema = create_engine("sqlite:///c:\sqlite3\inventorydb", echo=True)
db_schema = create_engine("sqlite:///c:\sqlite3\inventorydb", echo=True)
modelBase = declarative_base()

# +-------------------------+-------------------------+
# Student Biography Table
# +-------------------------+-------------------------+


class inventory(modelBase):
    __tablename__ = "INVENTORY2"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    inputer_name = Column(String)
    item_names = Column(String)
    description = Column(String)
    quantity = Column(Text)
    price   =  Column(Text)

    
# +-------------------------+-------------------------+
# Blog table schema
# +-------------------------+-------------------------+


class Reg(modelBase):

    __tablename__ = "user2"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    fname = Column(String)
    lname = Column(String)
    gender = Column(String)
    email = Column(String)
    passd = Column(String)
    date_created = Column(DateTime,
                          default=datetime.datetime.now())











# +-------------------------+-------------------------+
# +-------------------------+-------------------------+


def create_table():
    modelBase.metadata.create_all(db_schema)


def drop_table():
    modelBase.metadata.drop_all(db_schema)

# +-------------------------+-------------------------+
# +-------------------------+-------------------------+111111111111111111

# run this when you want to create the tables that you need for a project

if __name__ == '__main__':
    #LoginTable()
    create_table()
    #drop_table()
