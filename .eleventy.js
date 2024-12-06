const striptags = require('striptags');
const inspect = require('util').inspect;
const moment = require("moment");


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

	// site and backgrounds images and js
	eleventy.addPassthroughCopy("./src/imgs/");
	eleventy.addPassthroughCopy("./src/js/");
	eleventy.addPassthroughCopy("CNAME");
	eleventy.addPassthroughCopy("./src/favicon.ico");

	// load images from work folders
	eleventy.addPassthroughCopy("./src/work/**/*.jpg");
	eleventy.addPassthroughCopy("./src/work/**/*.jpeg");
	eleventy.addPassthroughCopy("./src/work/**/*.png");
	eleventy.addPassthroughCopy("./src/work/**/*.gif");

	// load blog assets
	eleventy.addPassthroughCopy("./src/assets/");

	// setup
	eleventy.addShortcode("excerpt", (content) => extractExcerpt(content));
	eleventy.addFilter("debug", (content) => `<pre>${inspect(content)}</pre>`);
	eleventy.addFilter("keys", (content) => `${Object.keys(content)}`);

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
			output: "./docs",
		}
	}
};