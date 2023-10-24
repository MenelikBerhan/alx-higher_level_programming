#!/usr/bin/node
/*
Script that writes a string to a file.
  The first argument is the file path
  The second argument is the string to write
  The content of the file will be written in utf-8
  If an error occurred during while writing, prints the error object
*/
const writeFile = require('fs').writeFile;
const path = process.argv[2];
const content = process.argv[3];
writeFile(path, content, 'utf-8', (err) => { if (err) console.log(err); });
