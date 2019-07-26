// configuración con el firebase
const config = {
  apiKey: "AIzaSyBXuy1tyZcsPd4fzi8PPY7111AAu9kK-yc",
  authDomain: "compra-facil-4d8c6.firebaseapp.com",
  databaseURL: "https://compra-facil-4d8c6.firebaseio.com",
  projectId: "compra-facil-4d8c6",
  storageBucket: "compra-facil-4d8c6.appspot.com",
  messagingSenderId: "117707978904",
  appId: "1:117707978904:web:8284144b82e359ee"
};
firebase.initializeApp(config);
// fin de la configuración con el firebase

const preObject = document.getElementById('object');

// Extraigo los datos de firebase, 'Precio_float'
const dbRefObject = firebase.database().ref().child('Precio_float');
const dbRefObject1 = firebase.database().ref().child('Marca');

dbRefObject.on('value', function(datasnapshot) {
  var datos = datasnapshot.val();
  preObject.innerText = datos[1];
});

dbRefObject1.on('value', function(datasnapshot) {
  var datosnombre = datasnapshot.val();
  console.log(datosnombre);
});


// Detectar el click de las imágenes
var uno = document.getElementById("uno");
var dos = document.getElementById("dos");
var tres = document.getElementById("tres");
var cuatro = document.getElementById("cuatro");

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