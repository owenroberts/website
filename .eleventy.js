const eleventySass = require("eleventy-sass");

module.exports = function(eleventyConfig) {
	eleventyConfig.ignores.add("_attachments");
	eleventyConfig.ignores.add("README.md");
	eleventyConfig.ignores.add("talk/slides/_jeks");
	
	// eleventyConfig.addPassthroughCopy("css");
	// eleventyConfig.addWatchTarget('css');

	eleventyConfig.addPassthroughCopy("imgs");
	eleventyConfig.addPassthroughCopy("favicon.ico");
	eleventyConfig.addPassthroughCopy("js");
	eleventyConfig.addPassthroughCopy("**/*.jpg");
	eleventyConfig.addPassthroughCopy("**/*.jpeg");
	eleventyConfig.addPassthroughCopy("**/*.png");
	eleventyConfig.addPassthroughCopy("**/*.gif");


	eleventyConfig.addPlugin(eleventySass);

	eleventyConfig.setLiquidOptions({
		timezoneOffset: 0,
	});
	
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
		}
	}
};