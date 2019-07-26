var list ={productos:[]};
var items = document.getElementsByClassName("item");
for(var i = 0; i < items.length; i++){
    items[i].addEventListener("click", function(e){
        list.productos.push(e.currentTarget.getAttribute("id"));
        console.log(list)
    });
}
document.getElementById("comparar").addEventListener("click", function(){
    localStorage.setItem("productos",JSON.stringify(list));
})
function agregarProducto(){
    
}
function quitarProducto(){

}
