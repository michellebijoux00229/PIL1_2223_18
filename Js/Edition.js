const ed = document.getElementById("edition");
const ev = document.getElementById("event");

ed.addEventListener("click", function(){
	document.getElementById("emploi").style = "display: block";
	document.querySelector("section h4").style = "display:none";
});
ev.addEventListener("click", function(){
	document.getElementById("evenement").style = "display:block";
	document.getElementById("emploi").style = "display:none";
	document.querySelector("section h4").style = "display:none";
});