#!/usr/bin/node
/*
Script that prints all characters of a Star Wars movie using the Star wars API:
  The first argument is the Movie ID - example: 3 = “Return of the Jedi”
  Displays one character name by line
*/
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (error, response, body) => {
        if (error) console.log(error);
        else console.log(JSON.parse(body).name);
      });
    }
  }
});
