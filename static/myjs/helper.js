addEventListener("blur", inputer_nameverify , true );
addEventListener("blur", item_nameverify, true);
addEventListener("blur", descriptionverify, true);
addEventListener("blur", quantityverify, true);
addEventListener("blur", priceverify, true);


function inputer_nameverify(){
    var _inputer_name = document.addeven.inputer_name;
    if (_inputer_name.value !=""){
        document.getElementById("inputer_name_r").textContent=""
        document.getElementById("inputer_name").style ="color:#5e6e66"
        return true
    }
}
function item_nameverify() {
    var _item_name = document.addeven.item_name;
    if (_item_name.value != "") {
        document.getElementById("item_name_r").textContent = ""
        document.getElementById("item_name").style = "color:#5e6e66"
        return true
    }
}

function descriptionverify() {
    var _description = document.addeven.description;
    if (_description.value != "") {
        document.getElementById("description_r").textContent = ""
        document.getElementById("description").style = "color:#5e6e66"
        return true
    }
}

function quantityverify() {
    var _quantity = document.addeven.quantity;
    if (_quantity.value != "") {
        document.getElementById("quantity_r").textContent = ""
        document.getElementById("quantity").style = "color:#5e6e66"
        return true
    }
}
function priceverify() {
    var _price = document.addeven.price;
    if (_price.value != "") {
        document.getElementById("price_r").textContent = ""
        document.getElementById("price").style = "color:#5e6e66"
        return true
    }
    return false
}


function _validate(){
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

// variables for registration


addEventListener("blur", fnameverify, true);
addEventListener("blur", lnameverify, true);
addEventListener("blur", genderverify, true);
addEventListener("blur", emailverify, true);
addEventListener("blur", password1verify, true);
addEventListener("blur", password2verify, true);
function fnameverify(){
    var fname = document.reg.fname;
    if (fname.value != ""){
        document.getElementById("fname").style = "color:#5e6e66"
        document.getElementById("fname_r").textContent=""
        return true    }
    }
    function lnameverify() {
        var lname = document.reg.lname;
        if (lname.value != "") {
            document.getElementById("lname").style = "color:#5e6e66"
            document.getElementById("lname_r").textContent = ""
            return true
        }
    }
    function genderverify() {
        var gender = document.reg.gender;
        if (gender.value != "") {
            document.getElementById("gender").style = "color:#5e6e66"
            document.getElementById("gender_r").textContent = ""
            return true
        }
    }
    function emailverify() {
        var email = document.reg.email;
        if (email.value != "") {
            document.getElementById("email").style = "color:#5e6e66"
            document.getElementById("email_r").textContent = ""
            return true
        }
    }
    
    function password1verify() {
        var password1 = document.reg.password1;
        if ((password1.value != "") && (password1.length > 5)) {
            document.getElementById("password1").style = "color:#5e6e66"
            document.getElementById("password1_r").textContent = ""
            return true
        }
}
function password2verify() {
    var password2 = document.reg.password2;
    if (password2.value != "")  {
        document.getElementById("password2").style = "color:#5e6e66"
        document.getElementById("password2_r").textContent = ""
        return true
    }
}

function reg_validation() {
    const _fname = document.reg.fname;
    const _lname = document.reg.lname;
    const _gender = document.reg.gender;
    const _email = document.reg.email;
    const _password1 = document.reg.password1;
    const _password2 = document.reg.password2;
if (_fname.value == "") {
        document.getElementById("fname_r").textContent = "Thsi Field is Required"
        document.getElementById("fname").style = "border:1px solid #dc3545"
        _fname.focus()
        return false
    }
    

if (_lname.value =="") {
        document.getElementById('lname_r').textContent ="Last Name Field Required"
        document.getElementById("lname").style = "border:1px solid #dc3545"
        _lname.focus()
        return false

    }

    if (_gender.value == "") {
        document.getElementById('gender_r').textContent ="Gender Name Field Required"
        document.getElementById("gender").style = "border:1px solid #dc3545"
        _gender.focus()
        return false    

    }
    if (_email.value == "") {
        document.getElementById('email_r').textContent = "Last Name Field Required"
        document.getElementById("email").style = "border:1px solid #dc3545"
        _email.focus()
        return false

    }
    if (_password1.value == "") {
        document.getElementById('password1_r').textContent = "Last Name Field Required"
        document.getElementById("password").style = "border:1px solid #dc3545"
        _password1.focus()
        return false
    }
     if (_password1.length <= 5 ) {
                document.getElementById('password1_r').textContent = "Password Too Weak"
                document.getElementById("password1").style = "border:1px solid #dc3545"
                _password1.focus()
                return false
        
            }
    if (_password2.value == "") {
        document.getElementById('password2_r').textContent = "Last Name Field Required"
        document.getElementById("password2").style = "border:1px solid #dc3545"
        _password2.focus()
        return false
    }

    if ((_password1.value) != (_password2.value)){
        document.getElementById("password2_r").textContent="Password Mismatch"
        document.getElementById("password2").style = "border:1px solid #dc3545"
        _password2.focus()
        return false
    }

 return true
}
     






// variables for registration
const fname = document.reg.fname;
const lname = document.reg.lname;
const gender = document.reg.gender;
const email = document.reg.email;
const password1 = document.reg.password1;
const password2 = document.reg.password2;


addEventListener("blur", fnameverify, true);
addEventListener("blur", lnameverify, true);
addEventListener("blur", genderverify, true);
addEventListener("blur", emailverify, true);
addEventListener("blur", password1verify, true);
addEventListener("blur", password2verify, true);
function fnameverify() {
    if (fname.value != "") {
        document.getElementById("fname").style = "color:#5e6e66"
        document.getElementById("fname_r").textContent = ""
        return true
    }
}
function lnameverify() {
    if (lname.value != "") {
        document.getElementById("lname").style = "color:#5e6e66"
        document.getElementById("lname_r").textContent = ""
        return true
    }
}
function genderverify() {
    if (gender.value != "") {
        document.getElementById("gender").style = "color:#5e6e66"
        document.getElementById("gender_r").textContent = ""
        return true
    }
}
function emailverify() {
    if (email.value != "") {
        document.getElementById("email").style = "color:#5e6e66"
        document.getElementById("email_r").textContent = ""
        return true
    }
}

function password1verify() {
    if (password1.value != "")  {
        document.getElementById("password1").style = "color:#5e6e66"
        document.getElementById("password1_r").textContent = ""
        return true
    }
}
function password2verify() {
    if (password2.value != "") {
        document.getElementById("password2").style = "color:#5e6e66"
        document.getElementById("password2_r").textContent = ""
        return true
    }
    return false
}
