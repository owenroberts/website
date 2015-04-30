window.onload = function() {
	var width = window.innerWidth;
	var bkg = document.getElementById('bkg');
	var img = new Image();
	img.src = 'imgs/eatingmachine00.png';
	bkg.appendChild(img);
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
		var xpos = ev.pageX;
		var num = Math.floor(xpos/columnWidth);
		img.src = 'imgs/' + imgs[num];
	}
};