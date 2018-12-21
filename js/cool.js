window.addEventListener('load', function() {
	String.prototype.replaceAt=function(index, character) {
    	return this.substr(0, index) + character + this.substr(index+character.length);
	}

	const titles = ["😬", "😑", "🌚", "😞", "😤"];
	var time = 500;
	var timer = Date.now();
	
	var b = document.querySelector("#butt");
	var t = b.innerHTML;
	
	function letterMove() {
		var n = Math.floor(Math.random() * t.length);
		var temp = t[n];
		var r = n;

		r +=  Math.round(Math.random()) ? -1 : 1;
		if (r > 0 && r < t.length) {
			var othertemp = t[r];
			t = t.replaceAt(n, othertemp);
			t = t.replaceAt(r, temp);
			b.innerText = t;
		}
	}
	
	function loop() {
		requestAnimationFrame(loop);
		if (Date.now() > timer + time) {
			timer = Date.now();
			document.title = titles[Math.floor(Math.random() * titles.length)];
			letterMove();
		}
	};
	requestAnimationFrame(loop);
});
