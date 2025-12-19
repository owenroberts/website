export default {
  url: process.env.ELEVENTY_ENV === 'dev' ? 
    'http://localhost:8080/website' : 
    'https://owen.cool',
};