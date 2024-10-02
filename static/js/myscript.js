$('.plus-cart').click(function () {
    // console.log('Plus Clicked')
    var id = $(this).attr('pid').toString();
    var quantity = this.parentNode.children[1];
    var amounts = document.getElementById('amount');
    var totalamounts = document.getElementById('totalamount');
    // console.log(id)
    $.ajax({
        type : "GET",
        url : "/pluscart",
        data : {
            prod_id : id,
        },
        success:function(data){
            quantity.innerText = data.quantity;
            amounts.innerText = data.amount;
            totalamounts.innerText = data.totalamount;
            // console.log('Success')
            // console.log(data.amount)
        }
    })
})

$('.minus-cart').click(function () {
    // console.log('Minus Clicked')
    var id = $(this).attr('pid').toString();
    var quantity = this.parentNode.children[1];
    var amounts = document.getElementById('amount');
    var totalamounts = document.getElementById('totalamount');
    // console.log(id)
    $.ajax({
        type : "GET",
        url : "/minuscart",
        data : {
            prod_id : id,
        },
        success:function(data){
            quantity.innerText = data.quantity;
            amounts.innerText = data.amount;
            totalamounts.innerText = data.totalamount;
            // console.log('Success')
        }
    })
})

$('.removecart').click(function () {
    // console.log('Minus Clicked')
    var id = $(this).attr('pid').toString();
    var ele = this
    var amounts = document.getElementById('amount');
    var totalamounts = document.getElementById('totalamount');
    // console.log(id)
    $.ajax({
        type : "GET",
        url : "/removecart",
        data : {
            prod_id : id,
        },
        success:function(data){
            amounts.innerText = data.amount;
            totalamounts.innerText = data.totalamount;
            console.log('DELETE')
            ele.parentNode.parentNode.parentNode.remove()
        }
    })
})




