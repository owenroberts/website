window.addEventListener('load', function() {
	String.prototype.replaceAt=function(index, character) {
    	return this.substr(0, index) + character + this.substr(index+character.length);
	}

	var title = "😬😬 😬😬"
	var alttitle = "😑🌚 😞😤";
	var time = 500;
	var timer = Date.now();
	
	var b = document.querySelector("#butt");
	var t = b.innerHTML;
	
	var letterMove = function() {
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
	
	var loop = function() {
		requestAnimationFrame(loop);
		if (Date.now() > timer + time) {
			timer = Date.now();
			if (document.title == title) document.title = alttitle;
			else document.title = title;
			letterMove();
		}
	};
	requestAnimationFrame(loop);
});
