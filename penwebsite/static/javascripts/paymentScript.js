$(document).ready(function(){

    var inner_price = document.getElementsByClassName('price_of_pens')
var inner_pen_quantity = document.getElementsByClassName('quantity_of_pen')
var inner_table_header = document.getElementsByClassName('table_headers')

for (i=0;i<inner_price.length;i++){
    if (parseInt(inner_price[i].placeholder)!=0){
        var table_row = document.createElement('TR')
        dynamic_id = 'myTr' + String(i)
        var table_row_id = table_row.setAttribute('id',dynamic_id)
        document.getElementById('parent_table').appendChild(table_row)
        
        for(j=0;j<inner_table_header.length;j++){
            var table_data = document.createElement('TD')
            dynamic_data_id = 'mtData' + String(j)
            var table_data_id = table_data.setAttribute('id',dynamic_data_id)
            
            if(j==0){
                var type_bought =  inner_pen_quantity[i].value
                var appending_type =  document.createTextNode(type_bought)
                table_data.appendChild(appending_type)
                
                document.getElementById(dynamic_id).appendChild(table_data)
                // document.getElementById(dynamic_data_id).style.textAlign = 'center'
                // var price = document.createTextNode(inner_price[i].placeholder)
                // table_data.appendChild(price)
                // document.getElementById('myTr').appendChild(table_data)
            }
            else if(j==1){
                var quantity_bought =  inner_pen_quantity[i].placeholder
                var appending_type = document.createTextNode(quantity_bought)
                table_data.appendChild(appending_type)
                
                document.getElementById(dynamic_id).appendChild(table_data)
                // document.getElementById(dynamic_data_id).style.textAlign = 'center'
            }
            else if(j==2){
                var total_cost =   inner_price[i].placeholder
                var cost_per_pice ='₹ ' + total_cost/inner_pen_quantity[i].placeholder.toString()
                var appending_type = document.createTextNode(cost_per_pice)
                table_data.appendChild(appending_type)
                
                document.getElementById(dynamic_id).appendChild(table_data)
                // document.getElementById(dynamic_data_id).style.textAlign = 'center'
            }

            else{

                var total_cost ='₹ ' +  inner_price[i].placeholder.toString()
                var appending_type =  document.createTextNode(total_cost)
                table_data.appendChild(appending_type)
                
                document.getElementById(dynamic_id).appendChild(table_data)
                // document.getElementById(dynamic_data_id).style.textAlign = 'center'
            }
        

        }
        
        
    
        

    }
}



document.getElementById('parent_table').style.textAlign='center'
let sum_of_cost=0
for(i=0;i<inner_price.length;i++){
    sum_of_cost=sum_of_cost+parseInt(inner_price[i].placeholder)
}

document.getElementById('Total_price').innerHTML='Grand Total is : ₹ '+(sum_of_cost).toString()
console.log(sum_of_cost)

// document.getElementById("credit_details").style.visibility = 'hidden'

// function show_func(){
//     document.getElementById("credit_details").style.visibility = 'visible'
// }

$("#payment_method").accordion() 

$("#card_input_field_number").keyup(function(){
   var input_val= ($("#card_input_field_number").val())
//    console.log(input_val)
//    if(parseInt(input_val)>=0 )
//    {
//        console.log("int wala ",parseInt(input_val))
//    }
   {
       var input_val = $("#card_input_field_number").val()
    //    console.log("hi",input_val)
       input_val = input_val.replace(/[a-zA-Z]+/g,'');
       $("#card_input_field_number").val(input_val) 
       console.log(input_val.length)
       if(input_val.length==4 || input_val.length==9 || input_val.length==14  ){
        $("#card_input_field_number").val( $("#card_input_field_number").val() + "-") 
        $("#card_input_field_number").attr("maxlength","19")
       }

   }
})

})
 