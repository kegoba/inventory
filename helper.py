{% extends "home.html" %}
{% block box %}

           <div class="row">
        <div class="col" style="text-align: center;">  EVENTORY RECORDS: </div>
    </div>  </br>
    <table class="table table-bordered">
        <thead>
            <tr>
                <td> ID </td>
                        <td> INPUTER NAME </td>
                        <td>ITEM NAME </td>
                        <td>DESCRIPTION</td>
                        <td>QUANTITY</td>
                        <td>PRICE</td>
                    </tr>
                </thead>
                <tbody>
                    <a href="{{url_for('.update_record')}}" >
                    {% for item in rec_  %}
                    <tr>  
                        <td> {{item[0] }} </td>
                        <td> {{item[1]}} </td>
                        <td> {{item[2]}} </td>
                        <td> {{item[3] }} </td>
                        <td> {{item[4] }} </td>
                        <td> {{item[5]}}  </td> 
                    </tr>
                    {% endfor %}
                    </a>
                </tbody>
            </table>

              <div class="container">
           <div class="row">
        <div class="col" style="text-align: center;">  EVENTORY RECORDS: </div>
    </div>  </br>
    {% for item in rec_ %}
    <div class="container" style="align-content: center; align-items: center">
        <div class="row">
    <a href=""class="list-group-item list-group-item-action flex-column align-items-start">
    <div class="col">
       {{ item[0] }}</h5>
    </div>
    <div class="col">
        {{ item[1] }}</h5>
    </div>
    <div class="col">
        {{ item[2] }}</h5>
    </div>
    <div class="col">
        {{ item[3] }}</h5>
    </div>
    <div class="col">
        {{ item[4] }}</h5>
    </div>
    <div class="col">
        {{ item[5] }}</h5>
    </div>
    
    <div class="col">
        <div style="color:blue"> <a href="{{url_for('.edith', id=item[0])}}"> Edith </a> </div>
    </div>
    <div class="col">
        <div clas="mb-1" style="color:red"> <a href="{{url_for('.delete', id=item[0])}}"> Delete</a> </div>
    </div>                   
     </div>
        
        </div>
    
    </div>


{% endblock %}

