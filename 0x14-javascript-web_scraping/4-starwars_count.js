#!/usr/bin/node
/*
Script that prints the number of movies where the character “Wedge Antilles” is present.
  The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
  Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
*/
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const films = JSON.parse(body).results;
    let total = 0;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.split('/').includes('18')) total++;
      }
    }
    console.log(total);
  }
});
