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

setInterval(function(){
	if(i < eventNumber){
		event[i].style="display:none";
		event[i+1].style="display:block";
		i=i+1;
	}
	if(i == eventNumber-1){
		setTimeout(function(){
			event[i].style="display:none";
			i = 0;
			event[i].style="display:block";
		},5000);
	}
},10000)