window.onload = function() {
	var width = window.innerWidth;
	var bkg = document.getElementById('bkg');
	var img = new Image();
	bkg.appendChild(img);
	var imgs = [];
	for (var i = 3; i < 143; i++) {
		if (i < 10) imgs.push("imgs/piggy/piggy"+0+0+0+i+".jpg");
		else if (i < 100) imgs.push("imgs/piggy/piggy"+0+0+i+".jpg");
		else imgs.push("imgs/piggy/piggy"+0+i+".jpg");
	}
	var columnWidth = width / imgs.length;
	console.log(imgs.length);
	console.log(Math.floor(Math.random()*imgs.length));
	img.src = imgs[Math.floor(Math.random()*imgs.length)];

	document.onmousemove = function(ev) {
		var xpos = ev.pageX;
		var num = Math.floor(xpos/columnWidth);
		img.src = imgs[num];
	}
};