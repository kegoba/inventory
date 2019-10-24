var _inputer_name = document.addeven.inputer_name;
var _item_name = document.addeven.item_name;
var _description = document.addeven.description;
var _quantity = document.addeven.quantity;
var _price = document.addeven.price;
addEventListener("blur", inputer_nameverify , true );
addEventListener("blur", item_nameverify, true);
addEventListener("blur", descriptionverify, true);
addEventListener("blur", quantityverify, true);
addEventListener("blur", priceverify, true);


function inputer_nameverify(){
    if (_inputer_name.value !=""){
        document.getElementById("inputer_name_r").textContent=""
        document.getElementById("inputer_name").style ="color:#5e6e66"
        return true
    }
}
function item_nameverify() {
    if (_item_name.value != "") {
        document.getElementById("item_name_r").textContent = ""
        document.getElementById("item_name").style = "color:#5e6e66"
        return true
    }
}

function descriptionverify() {
    if (_description.value != "") {
        document.getElementById("description_r").textContent = ""
        document.getElementById("description").style = "color:#5e6e66"
        return true
    }
}

function quantityverify() {
    if (_quantity.value != "") {
        document.getElementById("quantity_r").textContent = ""
        document.getElementById("quantity").style = "color:#5e6e66"
        return true
    }
}
function priceverify() {
    if (_price.value != "") {
        document.getElementById("price_r").textContent = ""
        document.getElementById("price").style = "color:#5e6e66"
        return true
    }
    return false
}


function _validate(event){
    var inputer_name = document.addeven.inputer_name;
    var item_name = document.addeven.item_name;
    var description = document.addeven.description;
    var quantity = document.addeven.quantity;
    var price = document.addeven.price;
    if (inputer_name.value =="")
    {
        document.getElementById("inputer_name_r").textContent = "Thsi Field is Required"
        document.getElementById("inputer_name").style = "border:1px solid #dc3545"
        inputer_name.focus()
        return false
    }
  if (item_name.value =="")
    {
      document.getElementById("item_name_r").textContent = "Thsi Field is Required"
       document.getElementById("item_name").style = "border:1px solid #dc3545"
        item_name.focus()
        return false
    }
    if (description.value == "") {
        document.getElementById("description_r").textContent = "Thsi Field is Required"
        document.getElementById("description").style = "border:1px solid #dc3545"
        description.focus()
        return false
    }
    if (quantity.value == "") {
        document.getElementById("quantity_r").textContent = "Thsi Field is Required"
        document.getElementById("quantity").style = "border:1px solid #dc3545"
        quantity.focus()
        return false
    }
    if (price.value == "") {
        document.getElementById("price_r").textContent = "Thsi Field is Required"
        document.getElementById("price").style = "border:1px solid #dc3545"
        price.focus()
        return false
    }
    

    return true
}


function reg_validation(event) {
    const fname_v = document.reg.fname;
    const lname_v = document.reg.lname;
    const gender_v = document.reg.gender;
    const email_v = document.reg.email;
    const password1_v = document.reg.password1;
    const password2_v = document.reg.password2;


    if (fname_v.value =="") {
        document.getElementById('fname_r').textContent = "Required";
        document.getElementById("fname").style = "border:1px solid #dc3545"
        fname_v.focus()
        return false
    }

    if (lname_v.value =="") {
        document.getElementById('lname_r').textContent ="Required"
        document.getElementById("lname").style = "border:1px solid #dc3545"
        lname_v.focus()
        return false

    }

    if (gender_v.value == "") {
        document.getElementById('gender_r').textContent ="Required"
        document.getElementById("gender").style = "border:1px solid #dc3545"
        gender_v.focus()
        return false    

    }
    if (email_v.value == "") {
        document.getElementById('email_r').textContent = "Required"
        document.getElementById("email").style = "border:1px solid #dc3545"
        email_v.focus()
        return false

    }
    if (password1_v.value == "") {
        document.getElementById('password1_r').textContent = "Required"
        document.getElementById("password1").style = "border:1px solid #dc3545"
        password1_v.focus()
        return false

    }
     
    if (password2_v.value == "") {
        document.getElementById('password2_r').textContent = "Required"
        document.getElementById("password2").style = "border:1px solid #dc3545"
        password2_v.focus()
        return false
    }

    if ((password1_v.value) != (password2_v.value)){
        document.getElementById("password2_r").textContent="Password Mismatch"
        document.getElementById("password2").style = "border:1px solid #dc3545"
        password2_v.focus()
        return false
    }

 return true
}

addEventListener("blur", fname_verify, true);
addEventListener("blur", lname_verify, true);
addEventListener("blur", gender_verify, true);
addEventListener("blur", email_verify, true);
addEventListener("blur", password1_verify, true);
addEventListener("blur", password2_verify, true);
function fname_verify() {
    const fname = document.reg.fname;
    if (fname.value != "") {
        document.getElementById("fname").style = "color:#5e6e66"
        document.getElementById("fname_r").textContent = ""
        return true
    }
}
function lname_verify() {
    const lname = document.reg.lname;
    if (lname.value != "") {
        document.getElementById("lname").style = "color:#5e6e66"
        document.getElementById("lname_r").textContent = ""
        return true
    }
}
function gender_verify() {
    const gender = document.reg.gender;
    if (gender.value != "") {
        document.getElementById("gender").style = "color:#5e6e66"
        document.getElementById("gender_r").textContent = ""
        return true
    }
}
function email_verify() {
    const email= document.reg.email;
    if (email.value != "") {
        document.getElementById("email").style = "color:#5e6e66"
        document.getElementById("email_r").textContent = ""
        return true
    }
}


function password1_verify() {
    const password1 = document.reg.password1;
    if (password1.value != "") {
        document.getElementById("password1").style = "color:#5e6e66"
        document.getElementById("password1").textContent = ""
        return true
    }
}
function password2_verify() {
    const password2= document.reg.password2;
    if (password2.value != "") {
        document.getElementById("password2").style = "color:#5e6e66"
        document.getElementById("password2_r").textContent = ""
        return true
    }
    return false
}