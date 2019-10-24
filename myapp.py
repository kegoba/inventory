from flask import (Flask, flash, render_template,app, request, session, redirect, url_for)
import datetime
app = Flask(__name__, template_folder="html_pages")
app.config.update(
    TESTING=True,
    SECRET_KEY=b'123'
)

from dbforms.db_cursor import sql_cursor
from dbforms.ormdb import inventory, Reg

@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/addeven.html', methods=["GET", "POST"])
def addeven():
    if request.method == 'POST':
        form = request.form

        _inputerf = form.get("inputer_name")
        item_field = form.get("item_name")
        _descriptionf = form.get("description")
        _quantityf = form.get("quantity")
        _pricef =  form.get("price")
        with sql_cursor() as db:
            ins = inventory()
            ins.inputer_name = _inputerf
            ins.item_names = item_field
            ins.description = _descriptionf   
            ins.quantity = _quantityf
            ins.price =   _pricef
            # inventory_table.date_created = datetime.datetime.now()
            db.add(ins)
           # flash("ITEM ADDED SUCCESSFULL")
    return render_template("addeven.html")



@app.route('/update', methods=["POST", "GET"])
def update_record():
    if request.method == 'POST':
        form = request.form
        inputer_field = form.get("inputer_field")
        item_field = form.get("item_field")
        description = form.get("description_field")
        quantity = form.get("quantity_field")
        price =     form.get("price_field")
        with sql_cursor() as db:
            db.query(
                inventory
            ).filter (
                inventory.id == request.form.get("id_v", int)
            ).update({
                        "inputer_name" : inputer_field,
                        "item_names":  item_field,
                        "description" : description,
                        "quantity" : quantity,
                        "price": price
                    })
        return render_template('update.html')
    return render_template("update.html")




@app.route('/delete', methods=["POST","GET"])
def delete_record():

   # import pdb; pdb.set_trace()
    if request.method == 'POST':
        with sql_cursor() as db:
            result1 = db.query(inventory).filter (
                    inventory.id == request.form.get("id_val", int)
                ).delete()
    return render_template("delete.html") 


@app.route("/search/update")
def search_update():
    qry = None

    with sql_cursor() as db:
        qry = db.query(
            inventory.item_names, inventory.description,
            inventory.inputer_name, inventory.quantity,  inventory.price, inventory.id
        ).filter(
            inventory.item_names.like("%" + request.args.get('search') + "%")
        ).first()

    return render_template("update.html", inputer_field=qry.inputer_name,
                               item_field=qry.item_names, price=qry.price,
                               description_field=qry.description,
                               quantity_field=qry.quantity, id_val=qry.id)


@app.route("/search/delete")
def search_item():

    qry = None

    with sql_cursor() as db:
        qry = db.query(
            inventory.item_names, inventory.description, inventory.price,
            inventory.inputer_name, inventory.quantity, inventory.id
        ).filter(
            inventory.item_names.like("%" + request.args.get('item_name') + "%")
        ).first()

    return render_template("delete.html", _inputerf=qry.inputer_name,
                               _item_field=qry.item_names, price=qry.price,
                               _description=qry.description,
                               _quantity=qry.quantity, id_val=qry.id)





@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        eror_msg = None
        form = request.form
        email = form.get("email")
        password = form.get("password")
        with sql_cursor() as db:
            qry = db.query(Reg.id, Reg.email, Reg.passd
            ).filter(
                (Reg.email) == email
            ).first()
            try:
                if (qry.passd) == password:
                    session["email"] = email
                    session["logged_in"] = True
                    #session["email"] = None
                    return redirect(url_for(".homepage"))
                else:
                    eror_msg ="Invalid username or password"
                    #if (qry.passd) != form.get("password"):
                    return render_template("login.html",  eror_msg=eror_msg)
            except:
                return render_template("login.html",  eror_msg=eror_msg)
 
    return render_template("login.html")



@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    
    return redirect(url_for(".login"))




@app.route("/view")
def _view_rec():
    if request.method == "GET":
        with sql_cursor() as db:
            qry = db.query(inventory.id, inventory.inputer_name, inventory.item_names,
                inventory.description, inventory.quantity, inventory.price
            ).all()
    return render_template("view.html", rec_= qry)

@app.route("/edith", methods=["POST"])
def update():
    if request.method == 'POST':
        form = request.form
        inputer_field = form.get("inputer")
        item_field = form.get("item")
        description = form.get("description")
        quantity = form.get("quantity")
        price =     form.get("price")
        with sql_cursor() as db:
            db.query(
                inventory
            ).filter (
                inventory.id == request.form.get("id_val")
            ).update({
                        "inputer_name" : inputer_field,
                        "item_names":  item_field,
                        "description" : description,
                        "quantity" : quantity,
                        "price": price
                    })
        return render_template('home.html')
    return render_template("home.html")


@app.route("/delete/<int:id>")
def delete(id):
    if request == "POST":
        form = request.form
        with sql_cursor as db:
            db.query(inventory).filter(
               (inventory.id) == (id, int)
            ).delete()
        redirect(url_for(".view_rec"))
    return render_template("view.html")




@app.route("/edith/<int:id>", methods=["GET"])
def edith(id):
    if request == "GET":        
        form = request.form
        inputer_field = form.get("inputer")
        item_field = form.get("item")
        description = form.get("description")
        quantity = form.get("quantity")
        price =     form.get("price")
        with sql_cursor() as db:
            db.query(
                inventory
            ).filter (
                inventory.id == request.form.get("id", int)
            ).update({
                        "inputer_name" : inputer_field,
                        "item_names":  item_field,
                        "description" : description,
                        "quantity" : quantity,
                        "price": price
                    })
        return render_template('edit.html')
    with sql_cursor() as db:
        qry = db.query(inventory.id, inventory.inputer_name, inventory.item_names,
                inventory.description, inventory.quantity, inventory.price).filter(
            inventory.id == id
        ).first()
    #print(qry)
    return render_template("edit.html", id = qry.id, inputer= qry.inputer_name, item = qry.item_names, quantity =qry.quantity,
                                        description=qry.description, price=qry.price)
            
    return render_template("edit.html")


        
    


@app.route("/reg", methods=["GET", "POST"])
def reg():
    inst = Reg()
    if request.method == "POST" :
        form = request.form
        fname = form.get("fname")
        lname = form.get("lname")
        gender = form.get("gender")
        email = form.get("email")
        password1 = form.get("password1")
        with sql_cursor() as db:
            inst.fname = fname
            inst.lname = lname
            inst.gender = gender
            inst.email = email
            inst.passd = password1
            db.add(inst)
            return render_template("login.html")      
    return render_template("reg.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6060, debug=True)



