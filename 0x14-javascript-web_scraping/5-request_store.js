#!/usr/bin/node
/*
Script that gets the contents of a webpage and stores it in a file.
  The first argument is the URL to request
  The second argument is the file path to store the body response
  The file will be UTF-8 encoded
*/
const request = require('request');
const writeFile = require('fs').writeFile;
const url = process.argv[2];
const path = process.argv[3];

request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    writeFile(path, body, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
