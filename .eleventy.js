// later -> https://davidea.st/articles/11ty-tips-i-wish-i-knew-from-the-start/


const eleventySass = require("eleventy-sass");
const inspect = require('util').inspect;
const striptags = require('striptags');

function extractExcerpt(content) {
	// https://www.jonathanyeong.com/garden/excerpts-with-eleventy/
	excerpt = striptags(content)
		.substring(0, 200) // Cap at 200 characters
		.replace(/^\s+|\s+$|\s+(?=\s)/g, "")
		.trim()
		.concat("...");
	return excerpt;
}


module.exports = function(eleventyConfig) {
	eleventyConfig.ignores.add("_attachments");
	eleventyConfig.ignores.add("README.md");
	eleventyConfig.ignores.add("talk/slides/_jeks");
	
	// eleventyConfig.addPassthroughCopy("css");
	// eleventyConfig.addWatchTarget('css');

	eleventyConfig.addPassthroughCopy("imgs/");
	eleventyConfig.addPassthroughCopy("assets/");
	eleventyConfig.addPassthroughCopy("lines/");


	eleventyConfig.addPassthroughCopy("favicon.ico");
	eleventyConfig.addPassthroughCopy("js/*.js");
	eleventyConfig.addPassthroughCopy("work/**/*.jpg");
	eleventyConfig.addPassthroughCopy("work/**/*.jpeg");
	eleventyConfig.addPassthroughCopy("work/**/*.png");
	eleventyConfig.addPassthroughCopy("work/**/*.gif");

	eleventyConfig.addFilter("debug", (content) => `<pre>${inspect(content)}</pre>`);
	eleventyConfig.addFilter("keys", (content) => `${Object.keys(content)}`);
	eleventyConfig.addShortcode("excerpt", (content) => extractExcerpt(content));

	eleventyConfig.addCollection('posts', collection =>
		collection.getFilteredByGlob(['_posts/*.html', '_posts/*.md'])
			.sort((a, b) => b.date - a.date)
	)
	
	eleventyConfig.addPlugin(eleventySass);
	eleventyConfig.setLiquidOptions({ timezoneOffset: 0, });
	
	eleventyConfig.setLiquidOptions({
		dynamicPartials: false,
		root: [
			'_includes',
			'.'
		]
	});
	
	return {
		dir: {
			input: "./",
			output: "./_site",
			layouts: "_layouts"
		},
		// templateFormats: ['md', 'html']
	}
};