const ed = document.getElementById("edition");
const ev = document.getElementById("event");
const ajout = document.getElementById("ajout");

ed.addEventListener("click", function(){
	document.getElementById("emploi").style = "display: block";
	document.querySelector(".welcom").style = "display:none";
	document.querySelector(".opt").style = "margin:10px 0";
});
ev.addEventListener("click", function(){
	document.getElementById("evenement").style = "display:block";
	document.getElementById("emploi").style = "display:none";
	document.querySelector(".welcom").style = "display:none";
	document.querySelector(".opt").style = "margin:10px 0";
});
