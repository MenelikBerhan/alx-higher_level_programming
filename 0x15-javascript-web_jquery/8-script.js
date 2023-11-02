// a JavaScript script that fetches and lists the title for all movies by using
// this URL: https://swapi-api.alx-tools.com/api/films/?format=json
// All movie titles will be list in the HTML tag UL#list_movies
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, (data) => {
  for (const movie of data.results) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  }
});
