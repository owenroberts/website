$(document).ready(function() {
	var	audio =  	document.getElementById('audio'),
		startBtn = 	document.querySelector('#start'),
		prevBtn = 	document.querySelector('#prev'),
		nextBtn = 	document.querySelector('#next'),
		playBtn = document.querySelector('#play'),
		progress = document.querySelector('#progress'),
		bar = document.querySelector('#bar'),
		progressTotal = document.querySelector('#progress').offsetWidth,
		playhead = document.querySelector('#playhead')
		;

	var currentFrame = 1, numFrames = 24;

	var h = location.hash.split("#")[1];
	if (h) currentFrame = h;

	var update = function(frame) {

		if (frame == "start") currentFrame = 1;
		if (frame == "next") {
			if (currentFrame < numFrames) currentFrame++;
		}
		if (frame == "prev") {
			if (currentFrame > 1) currentFrame--;
		}
		if (currentFrame == 1) {
			startBtn.style.display 	= 'none';
			prevBtn.style.display 	= 'none';
		} else {
			startBtn.style.display 	= 'inline';
			prevBtn.style.display 	= 'inline';
		}
		if (currentFrame == numFrames) nextBtn.style.display = 'none';
		else  nextBtn.style.display = 'inline';

		loadAnimation(currentFrame);
		audio.src = "clips/" + currentFrame + ".mp3";
		audio.play();
		playBtn.innerHTML = '❚❚';

		location.hash = '#'+currentFrame;
	}

	startBtn.onclick 	= function() { update("start"); };
	prevBtn.onclick 	= function() { update("prev"); };
	nextBtn.onclick 	= function() { update("next"); };

	update();

	playBtn.addEventListener('click', function() {
		if ( audio.paused ) {
			audio.play();
			playBtn.innerHTML = '❚❚';
		} else {
			audio.pause();
			playBtn.innerHTML = '▶';
		}
	});
	//update progress using requestAnimationFrame
	function step() {
		var progressRatio = audio.currentTime / audio.duration;
		bar.style.right = progressTotal - progressRatio * progressTotal + "px";
		window.requestAnimationFrame( step );
	}
	window.requestAnimationFrame( step );

	audio.addEventListener('ended', function() {
		playBtn.innerHTML = '▶';
	});
	progress.addEventListener('click', function(ev) {
		var ratio = (ev.clientX - ev.currentTarget.getBoundingClientRect().left) / progressTotal;
		console.log(ratio * audio.duration);
		audio.currentTime = ratio * audio.duration;
	});
	progress.addEventListener('mousemove', function(ev) {
		playhead.style.opacity = 1;
		if (ev.offsetX > 5)	
			playhead.style.left = ev.offsetX + "px";
	});
	progress.addEventListener('mouseout', function(ev) {
		playhead.style.opacity = 0;
	});
});