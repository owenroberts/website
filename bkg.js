window.onload = function() {
	var width = window.innerWidth;
	var bkg = document.getElementById('bkg');
	var imgs = [];
	for (var i = 3; i < 143; i++) {
		var img = new Image();
		if (i < 10) 		img.src = "imgs/piggy/piggy"+0+0+0+i+".jpg";
		else if (i < 100) 	img.src = "imgs/piggy/piggy"+0+0+i+".jpg";
		else 				img.src = "imgs/piggy/piggy"+0+i+".jpg";
		imgs.push(img);
	}
	var columnWidth = width / imgs.length;
	bkg.appendChild(imgs[Math.floor(Math.random()*imgs.length)]);

	document.onmousemove = function(ev) {
		var xpos = ev.pageX;
		var num = Math.floor(xpos/columnWidth);
		bkg.removeChild(bkg.firstChild);
		bkg.appendChild(imgs[num]);
	}
};