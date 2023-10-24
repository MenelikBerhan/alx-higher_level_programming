#!/usr/bin/node
/*
Script that prints all characters of a Star Wars movie using the Star wars API:
  The first argument is the Movie ID - example: 3 = “Return of the Jedi”
  Displays one character name by line in the same order of the list “characters” in the /films/ response
*/
const request = require('request');
const util = require('util');
const requestPromise = util.promisify(request); // to promisify request so we can use await

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// an async function needed to use await
// (await is only valid in async functions and the top level bodies of modules)
async function main () {
  let response = await requestPromise(url);
  const characters = JSON.parse(response.body).characters;
  for (const character of characters) {
    response = await requestPromise(character);
    console.log(JSON.parse(response.body).name);
  }
}

main();
