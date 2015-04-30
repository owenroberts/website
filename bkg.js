window.onload = function() {
	var width = window.innerWidth;
	var imgs = [ 
	"eatingmachine00.png",
	"eatingmachine01.png",
	"eatingmachine02.png",
	"eatingmachine03.png",
	"eatingmachine04.png",
	"eatingmachine05.png",
	"eatingmachine06.png",
	"eatingmachine07.png",
	"eatingmachine08.png",
	"eatingmachine09.png"
	];
	var columnWidth = width / imgs.length;
	document.onmousemove = function(ev) {
		var pos = ev.pageX;
		var num = Math.floor(pos/columnWidth);
		document.body.style.backgroundImage = 'url(imgs/eatingmachine0' + num + '.png)';

	}
};