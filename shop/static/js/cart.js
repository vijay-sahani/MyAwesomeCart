if (localStorage.getItem('cart') == null) {
    var cart = {};
}
else {
    cart = JSON.parse(localStorage.getItem('cart'));
    updateCart(cart);
}
$('.cart').click(function () {
    var idstr = this.id.toString()
    console.log(idstr)
    if (cart[idstr] != undefined) {
        qty= cart[idstr] + 1;
    } else {
        qty= 1;
        pro_name=document.getElementById('name'+idstr).innerHTML;
        price=document.getElementById('price'+idstr).innerHTML;
        cart[idstr]=[qty,pro_name,price];
    }
    updateCart(cart,idstr);
})


function updateCart(cart,id=undefined){
    let sum=0;
    for (let item in cart){
        sum+=cart[item][0];
    }
    if (id!=undefined){
        document.getElementById('div'+id).innerHTML=`<button id="minus${id}" class="btn btn-primary minus">-</button><span id="val${id}">${cart[id][0]}</span><button id="plus${id}" class="btn btn-primary plus">+</button>`;
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cartItem').innerHTML =sum;
    }
// Minus and plus button
$('.divpr').on('click','button.minus',function(){
    let int =this.id.slice(7,);
    cart['pr'+int][0]=cart['pr'+int][0]-1;
    cart['pr'+int][0]=Math.max(0,cart['pr'+int][0]);
    cart['pr'+int][0]=document.getElementById('valpr'+int).innerHTML=cart['pr'+int][0];
    updateCart(cart,'pr'+int);
})
$('.divpr').on('click','button.plus',function(){
    let int =this.id.slice(6,);
    cart['pr'+int][0]=document.getElementById('valpr'+int).innerHTML=cart['pr'+int][0]+1;
    updateCart(cart,'pr'+int);
})


