Naavy = {
  setup: function() {       
    Naavy.pages.forEach( function(page) {
        var link = $( '<a>' ).attr('href', page[1]).html(page[0]);
				if (page[0] == 'the eating machine dot com' || page[0]=='teaching') { link.append('<br>')};
        $( 'nav' ).append( link );
    }); 
		$('nav').append('<br>contact: owen at theeatingmachine<br>dot com<hr>');
  },
  pages: [
    ['the eating machine dot com', '/index.html'],
    ['blog', 'blog/'],
		['work', '/work.html'],
		['teaching', '/teaching.html'],
		['github', 'http://www.github.com/owenroberts'],
    ['tumblr', '/tumblr.html'],
		['instagram', 'http://instagram.com/owenribbit']
		
  ],
}
$( document ).ready( Naavy.setup )