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

var nameHTML, priceHTML, producto, tienda, place, largo;
var costoTotal;

var i;

function MostrarDatos(place, nameHTML, priceHTML, i, producto, tienda, largo, placeTotal)
{
  var price = [];
  var minimo;
  // Extraigo los datos de firebase, 'Precio_float'
  // const dbRefObject1 = firebase.database().ref().child('Marca');
  var divName = document.getElementById(nameHTML);
  var divPrice = document.getElementById(priceHTML);
  var totalCost = document.getElementById(placeTotal);
  
  for (i = 0; i < largo; i++)
  {
    const dbRefObject = firebase.database().ref().child(`${place}/${tienda}/${producto}/${producto}${i}/Precio_float`);
    
    dbRefObject.on('value', function(datasnapshot) {
      price.push(parseFloat(datasnapshot.val()));
      // console.log(price);
      
      if (price.length == largo)
      {
        minimo = Math.min.apply(null, price);
        divPrice.innerText = minimo;
        // console.log(minimo);

        // Guardo el total en una variable 'total' para luego cortarlo solo a dos decimales
        var total = parseFloat(totalCost.innerText) + minimo;
        // Aquí abajo lo corto con .toFixed(cantidad):
        totalCost.innerText = total.toFixed(2); 
        
        // Aquí le saco el índice del lugar dónde se encuentra alojado el mínimo en el array price[]
        // Para luego usarlo en la extracción del nombre al que le corresponde dicho valor (minimo)
        var indice = (price.indexOf(minimo));
        // console.log(indice);

        const dbRefObject1 = firebase.database().ref().child(`${place}/${tienda}/${producto}/${producto}${indice}/Producto`);
        dbRefObject1.on('value', function(datasnapshot) {
          // console.log(datasnapshot.val());
          divName.innerText = datasnapshot.val();
        });
      }
    });
  }
}

place = 'Supermercados';



tienda = 'Metro';
placeTotal = "totalMetro";

nameHTML = "leche-metro-name";
priceHTML = "leche-metro-price";
producto = 'Lacteos';
largo = 449;
MostrarDatos(place, nameHTML, priceHTML, i, producto, tienda, largo, placeTotal);
nameHTML = "azucar-metro-name";
priceHTML = "azucar-metro-price";
producto = 'Azucar';
largo = 61;
MostrarDatos(place, nameHTML, priceHTML, i, producto, tienda, largo, placeTotal);
nameHTML = "aceite-metro-name";
priceHTML = "aceite-metro-price";
producto = 'Aceites';
largo = 54;
MostrarDatos(place, nameHTML, priceHTML, i, producto, tienda, largo, placeTotal);
nameHTML = "arroz-metro-name";
priceHTML = "arroz-metro-price";
producto = 'Arroces';
largo = 35;
MostrarDatos(place, nameHTML, priceHTML, i, producto, tienda, largo, placeTotal);

tienda = 'Tottus';
placeTotal = "totalTottus";

nameHTML = "leche-tottus-name";
priceHTML = "leche-tottus-price";
producto = 'Lacteos';
largo = 20;
MostrarDatos(place, nameHTML, priceHTML, i, producto, tienda, largo, placeTotal);
nameHTML = "azucar-tottus-name";
priceHTML = "azucar-tottus-price";
producto = 'Azucar';
largo = 38;
MostrarDatos(place, nameHTML, priceHTML, i, producto, tienda, largo, placeTotal);
nameHTML = "aceite-tottus-name";
priceHTML = "aceite-tottus-price";
producto = 'Aceites';
largo = 85;
MostrarDatos(place, nameHTML, priceHTML, i, producto, tienda, largo, placeTotal);
nameHTML = "arroz-tottus-name";
priceHTML = "arroz-tottus-price";
producto = 'Arroces';
largo = 47;
MostrarDatos(place, nameHTML, priceHTML, i, producto, tienda, largo, placeTotal);

tienda = 'Wong';
placeTotal = "totalWong";

nameHTML = "leche-wong-name";
priceHTML = "leche-wong-price";
producto = 'Lacteos';
largo = 697;
MostrarDatos(place, nameHTML, priceHTML, i, producto, tienda, largo, placeTotal);
nameHTML = "azucar-wong-name";
priceHTML = "azucar-wong-price";
producto = 'Azucar';
largo = 68;
MostrarDatos(place, nameHTML, priceHTML, i, producto, tienda, largo, placeTotal);
nameHTML = "aceite-wong-name";
priceHTML = "aceite-wong-price";
producto = 'Aceites';
largo = 89;
MostrarDatos(place, nameHTML, priceHTML, i, producto, tienda, largo, placeTotal);
nameHTML = "arroz-wong-name";
priceHTML = "arroz-wong-price";
producto = 'Arroces';
largo = 35;
MostrarDatos(place, nameHTML, priceHTML, i, producto, tienda, largo, placeTotal);
