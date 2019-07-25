
// var fireHeading = document.getElementById("banner");
var fireHeading = document.querySelector('.banner');
// fireHeading.innerText = "hola";

// var database = firebase.firestore();

var fireHeadingRef = firebase.database().auth().child();
// alert(database.ref("Price"));
  
fireHeadingRef.on('value', function(datasnapshot) {
  // console.log(datasnapshot.val());
  fireHeading.innerText = datasnapshot.val();
});