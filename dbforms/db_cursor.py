"""
    Database cursor script to handle transactions with the database
    sqlalchemy documentation link ==>
        http://docs.sqlalchemy.org/en/latest/orm/tutorial.html

"""

from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker

# +-------------------------+-------------------------+
# User defined imports
# +-------------------------+-------------------------+

from dbforms.ormdb import db_schema, inventory  # imported from the orm_dataaccess.py file

# +-------------------------+-------------------------+
# +-------------------------+-------------------------+

CursorObj = sessionmaker(bind=db_schema)

# +-------------------------+-------------------------+
# +-------------------------+-------------------------+

@contextmanager  # decorator to handle database connections
def sql_cursor():
    cursor = CursorObj()

    yield cursor

    try:
        cursor.commit()
    except Exception as e:
        cursor.rollback()
        raise e
        # add a logger here


# +-------------------------+-------------------------+
# +-------------------------+-------------------------+


def test_record_insert():
    student = INVENTORY_TB()
    student.fname = 'jeff'
    student.sname = 'uzodinma'
    student.age = 1
    student.address = '7, ashaye street, obawole, lagos nigeria'

    with sql_cursor() as db:
        db.add(student)

# +-------------------------+-------------------------+
# +-------------------------+-------------------------+

def test_record_select():

    print(output)
    with sql_cursor() as db:
        output = db.query(Student.fname, Student.sname
                ).filter(
                    Student.fname == 'jeff'
                ).first()


# +-------------------------+-------------------------+
# +-------------------------+-------------------------+

def test_record_update():
    with sql_cursor() as db:
        db.query(Student).filter(
            INVENTORY.sname == 'uzodinma'
        ).update({'age': 30})

# +-------------------------+-------------------------+
# +-------------------------+-------------------------+

def test_record_delete():
    with sql_cursor() as db:
        db.query(INVENTORY).filter(INVENTORY.fname == 'jeff').delete()


# +-------------------------+-------------------------+
# +-------------------------+-------------------------+

if __name__ == '__main__':
    # test_record_insert()  ## let insert a first record
    # test_record_select()  # lets select the newly created record
    # test_record_update() # lets update a record on the table
    test_record_delete()  # lets delete the records from the database
