// Detectar el click de las imágenes
var uno = document.getElementById("leche");
var dos = document.getElementById("aceite");
var tres = document.getElementById("azucar");
var cuatro = document.getElementById("arroz");

uno.addEventListener('click', selectAnimationUno);
dos.addEventListener('click', selectAnimationDos);
tres.addEventListener('click', selectAnimationTres);
cuatro.addEventListener('click', selectAnimationCuatro);

function selectAnimationUno() {
  if(uno.classList.contains('is-active')) 
  {
    uno.classList.remove('is-active');
    uno.classList.add('select');
  }
  else 
  {
    uno.classList.add('is-active');
    uno.classList.remove('select');
  }
}
function selectAnimationDos() {
  if(dos.classList.contains('is-active')) 
  {
    dos.classList.remove('is-active');
    dos.classList.add('select');
  }
  else 
  {
    dos.classList.add('is-active');
    dos.classList.remove('select');
  }
}
function selectAnimationTres() {
  if(tres.classList.contains('is-active')) 
  {
    tres.classList.remove('is-active');
    tres.classList.add('select');
  }
  else 
  {
    tres.classList.add('is-active');
    tres.classList.remove('select');
  }
}
function selectAnimationCuatro() {
  if(cuatro.classList.contains('is-active')) 
  {
    cuatro.classList.remove('is-active');
    cuatro.classList.add('select');
  }
  else 
  {
    cuatro.classList.add('is-active');
    cuatro.classList.remove('select');
  }
}

// FERNANDO
var list ={productos:[]};
var items = document.getElementsByClassName("item");
for(var i = 0; i < items.length; i++){
    items[i].addEventListener("click", function(e){
        list.productos.push(e.currentTarget.getAttribute("id"));
        // console.log(list)
    });
}
document.getElementById("comparar").addEventListener("click", function(){
    localStorage.setItem("productos",JSON.stringify(list));
})