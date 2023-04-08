// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO"); //prints AYO to console

var i = "hello"; //looks like a variable
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) { //variables can now be functions? how do we call this function?
  //this function looks like it adds 30 to whatever argument you provide
  var j=30;
  return j+x;
};
console.log(f(100)) //calls the function

//instantiate an object
//looks like a dictionary
var o = { 'name' : 'Thluffy',
          age : 1024, //why does this not have quotes around it
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

console.log(o.randomNotEvenThere) //undefined
console.log(o.func(30)); //60
console.log(o.func); //code for the function
console.log(o.name); //Thluffy
console.log(o); //'name' just becomes name


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

addItem("hello world") //hello world is appended to the end of the list, inside of an li container

var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  console.log(listitems); //HTMLCollection object that can be indexed
  listitems[n].remove();
};
removeItem(3)

var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    console.log(items[i].classList); //DOMTokenList
    items[i].classList.add('red');
  }
};
red()


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

stripe()

//insert your implementations here for...
// FIB
// FAC
// GCD

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};


