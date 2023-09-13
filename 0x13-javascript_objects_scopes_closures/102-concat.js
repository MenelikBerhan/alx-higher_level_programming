#!/usr/bin/node
const fs = require('fs');
console.log('./' + process.argv[2]);
fs.readFile(process.argv[2],
  // callback function that is called when reading file is done
  function (err, data) {
    if (err) throw err;
    // data is a buffer containing file content
    // console.log(data.toString('utf8'))
    fs.writeFile(process.argv[4], data, function (err) {
      if (err) throw err;
      // console.log('File is created successfully.');
    });
  });

fs.readFile(process.argv[3],
  // callback function that is called when reading file is done
  function (err, data) {
    if (err) throw err;
    // data is a buffer containing file content
    // console.log(data.toString('utf8'))
    fs.appendFile(process.argv[4], data, function (err) {
      if (err) throw err;
      // console.log('File is updated successfully.');
    });
  });
