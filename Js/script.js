const connecter = document.getElementById("connect");
const eventArray = document.querySelectorAll("#event div");
const closeFormBtn = document.querySelector("#form span");
const event = document.querySelectorAll("#event div");
const eventNumber = event.length;
let i = 0;

connecter.addEventListener("click", function(){
	document.getElementById("form").style = "display:block";
});
closeFormBtn.addEventListener("click", function(){
	document.getElementById("form").style = "display:none";
});
