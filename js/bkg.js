window.addEventListener('load', function() {

	// ** check for mobile ** http://www.abeautifulsite.net/detecting-mobile-devices-with-javascript/
	var isMobile = {
	    Android: function() {
	        return navigator.userAgent.match(/Android/i);
	    },
	    BlackBerry: function() {
	        return navigator.userAgent.match(/BlackBerry/i);
	    },
	    iOS: function() {
	        return navigator.userAgent.match(/iPhone|iPad|iPod/i);
	    },
	    Opera: function() {
	        return navigator.userAgent.match(/Opera Mini/i);
	    },
	    Windows: function() {
	        return navigator.userAgent.match(/IEMobile/i);
	    },
	    any: function() {
	        return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
	    }
	};

	var numImages;

	if (isMobile.any()) {
		numImages = 6;
	} {
		numImages = 143;
	}
	
	var bkg = document.getElementById('bkg');

	var width = bkg.offsetWidth;
	var imgs = [];
	for (var i = 3; i < numImages; i++) {
		var img = new Image();
		if (i < 10) 		img.src = "imgs/piggy/piggy"+0+0+0+i+".jpg";
		else if (i < 100) 	img.src = "imgs/piggy/piggy"+0+0+i+".jpg";
		else 				img.src = "imgs/piggy/piggy"+0+i+".jpg";
		imgs.push(img);
		bkg.appendChild(img);
		bkg.removeChild(img);
	}
	var columnWidth;
	var setSize = function() {
		columnWidth = window.innerWidth / imgs.length;
	}
	setSize();
	bkg.appendChild(imgs[Math.floor(Math.random()*imgs.length)]);

	if (!isMobile.any()) {
		document.onmousemove = function(ev) {
			var xpos = ev.pageX;
			var num = Math.floor(xpos/columnWidth);
			bkg.removeChild(bkg.firstChild);
			bkg.appendChild(imgs[num]);
		}
		window.onresize = function(ev) {
			setSize();
		}
	}

});