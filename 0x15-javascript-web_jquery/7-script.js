#!/usr/bin/node
// a JavaScript script that fetches the character name from this
// URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
// The name will be displayed in the HTML tag DIV#character
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, (data) => {
  $('div#character').text(data.name);
});
