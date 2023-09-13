#!/usr/bin/node
const dict = require('./101-data').dict;
const dictNew = {};

for (const key in dict) {
  if (dictNew[dict[key]]) dictNew[dict[key]].push(key);
  else dictNew[dict[key]] = [key];
}
console.log(dictNew);
