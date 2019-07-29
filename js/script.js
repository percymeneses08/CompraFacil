var superW = document.getElementById("wong").children[1].children[1].children;
var superM = document.getElementById("metro").children[1].children[1].children;
var superT = document.getElementById("tottus").children[1].children[1].children;
var productosSeleccionados = localStorage.getItem("productos");
productosSeleccionados = JSON.parse(productosSeleccionados);
console.log(productosSeleccionados);
var price = 0;
for(var i = 0; i < superW.length; i++){
    price = parseFloat(superW[i].innerText) + price;
    console.log(superW[i].innerText)
}

document.getElementById("totalWong").innerText = price;