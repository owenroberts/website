const { EleventyHtmlBasePlugin } = require("@11ty/eleventy");
const striptags = require('striptags');
const inspect = require('util').inspect;
const moment = require("moment");
const { JSDOM } = require("jsdom");


function extractExcerpt(content) {
	// https://www.jonathanyeong.com/garden/excerpts-with-eleventy/
	excerpt = striptags(content)
		.substring(0, 80) // Cap at 200 characters
		.replace(/^\s+|\s+$|\s+(?=\s)/g, "")
		.trim()
		.concat("...");
	return excerpt;
}

module.exports = function(eleventy) {

	eleventy.addPlugin(EleventyHtmlBasePlugin);

	// site and backgrounds images and js
	eleventy.addPassthroughCopy("./src/imgs/");
	eleventy.addPassthroughCopy("./src/css/");
	eleventy.addPassthroughCopy("./src/js/");
	eleventy.addPassthroughCopy("./src/favicon.ico");
	
	eleventy.addPassthroughCopy("CNAME");
	eleventy.addPassthroughCopy(".nojekyll");

	// load blog assets
	eleventy.addPassthroughCopy("./src/assets/");

	// setup
	eleventy.addShortcode("excerpt", (content) => extractExcerpt(content));
	eleventy.addFilter("debug", (content) => `<pre>${inspect(content)}</pre>`);
	eleventy.addFilter("keys", (content) => `${Object.keys(content)}`);

	const url = process.env.ELEVENTY_ENV === 'dev' ? 
		'http://localhost:8080/website' : 
		'https://owen.cool';

	eleventy.addTransform("prependImageUrl", (content, outputPath) => {
		if (outputPath && outputPath.endsWith(".html") && outputPath.includes("/work/")) {
			// console.log(outputPath);
			let dom = new JSDOM(content);
			let document = dom.window.document;

			let images = document.querySelectorAll("img");
			images.forEach(image => {
				let src = image.getAttribute("src");
				if (!src.includes("http")) {
					
					image.setAttribute("src", `${url}/assets/${src}`);
				}
			});

	      return dom.serialize();
	    }
	    return content;
	});

	eleventy.addCollection('archive', collection =>
		collection.getFilteredByGlob([
			'src/archive/doodoo/fposts/*.html',
			'src/archive/idtio/fposts/*.html',
			'src/archive/twitter/fposts/*.html',
		])
		.filter(item => !item.data.categories.includes('RT'))
		.filter(item => !item.data.categories.includes('instagram'))
		.sort((a, b) => b.date - a.date)
	);

	eleventy.addCollection('doodoo', collection =>
		collection.getFilteredByGlob([
			'src/archive/doodoo/fposts/*.html'
		])
		.filter(item => !item.data.categories.includes('instagram'))
		.sort((a, b) => b.date - a.date)
	);

	eleventy.addCollection('idtio', collection =>
		collection.getFilteredByGlob([
			'src/archive/idtio/fposts/*.html'
		])
		.sort((a, b) => b.date - a.date)
	);

	eleventy.addCollection('terrible_nfts', collection =>
		collection.getFilteredByGlob([
			'src/archive/terrible_nfts/fposts/*.html'
		])
		.sort((a, b) => b.date - a.date)
	);

	eleventy.addCollection('twitter', collection =>
		collection.getFilteredByGlob([
			'src/archive/twitter/fposts/*.html'
		])
		.filter(item => !item.data.categories.includes('RT'))
		.sort((a, b) => b.date - a.date)
	);

	eleventy.setLiquidOptions({
		dynamicPartials: false,
	});

	eleventy.addFilter("toUTCString", (date) => {
		const utc = date.toUTCString();
		return moment.utc(utc).format("MMMM D, YYYY");
	});

	return {
		dir: {
			input: "./src",
		},
		pathPrefix: "/website/"
	}
};