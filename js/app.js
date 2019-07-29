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

var nameHTML, productoHTML, producto, tienda, place, largo;

var i;


function MostrarDatos(place, nameHTML, productoHTML, i, producto, tienda, largo)
{
  var price = [];
  var minimo;
  // Extraigo los datos de firebase, 'Precio_float'
  // const dbRefObject1 = firebase.database().ref().child('Marca');
  var divName = document.getElementById(nameHTML);
  var divPrice = document.getElementById(productoHTML);
  
  for (i = 0; i < largo; i++)
  {
    const dbRefObject = firebase.database().ref().child(`${place}/${tienda}/${producto}/${producto}${i}/Precio_float`);
    
    dbRefObject.on('value', function(datasnapshot) {
      price.push(parseFloat(datasnapshot.val()));
      // console.log(price);
      minimo = Math.min.apply(null, price);
      divPrice.innerText = minimo;

      if (price.length == largo)
      {
        // console.log(minimo);
        
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

nameHTML = "leche-metro-name";
productoHTML = "leche-metro-price";
producto = 'Lacteos';
largo = 449;
MostrarDatos(place, nameHTML, productoHTML, i, producto, tienda, largo);
nameHTML = "azucar-metro-name";
productoHTML = "azucar-metro-price";
producto = 'Azucar';
largo = 61;
MostrarDatos(place, nameHTML, productoHTML, i, producto, tienda, largo);
nameHTML = "aceite-metro-name";
productoHTML = "aceite-metro-price";
producto = 'Aceites';
largo = 54;
MostrarDatos(place, nameHTML, productoHTML, i, producto, tienda, largo);
nameHTML = "arroz-metro-name";
productoHTML = "arroz-metro-price";
producto = 'Arroces';
largo = 35;
MostrarDatos(place, nameHTML, productoHTML, i, producto, tienda, largo);

tienda = 'Tottus';

nameHTML = "leche-tottus-name";
productoHTML = "leche-tottus-price";
producto = 'Lacteos';
largo = 20;
MostrarDatos(place, nameHTML, productoHTML, i, producto, tienda, largo);
nameHTML = "azucar-tottus-name";
productoHTML = "azucar-tottus-price";
producto = 'Azucar';
largo = 38;
MostrarDatos(place, nameHTML, productoHTML, i, producto, tienda, largo);
nameHTML = "aceite-tottus-name";
productoHTML = "aceite-tottus-price";
producto = 'Aceites';
largo = 85;
MostrarDatos(place, nameHTML, productoHTML, i, producto, tienda, largo);
nameHTML = "arroz-tottus-name";
productoHTML = "arroz-tottus-price";
producto = 'Arroces';
largo = 47;
MostrarDatos(place, nameHTML, productoHTML, i, producto, tienda, largo);

tienda = 'Wong';

nameHTML = "leche-wong-name";
productoHTML = "leche-wong-price";
producto = 'Lacteos';
largo = 697;
MostrarDatos(place, nameHTML, productoHTML, i, producto, tienda, largo);
nameHTML = "azucar-wong-name";
productoHTML = "azucar-wong-price";
producto = 'Azucar';
largo = 68;
MostrarDatos(place, nameHTML, productoHTML, i, producto, tienda, largo);
nameHTML = "aceite-wong-name";
productoHTML = "aceite-wong-price";
producto = 'Aceites';
largo = 89;
MostrarDatos(place, nameHTML, productoHTML, i, producto, tienda, largo);
nameHTML = "arroz-wong-name";
productoHTML = "arroz-wong-price";
producto = 'Arroces';
largo = 35;
MostrarDatos(place, nameHTML, productoHTML, i, producto, tienda, largo);
