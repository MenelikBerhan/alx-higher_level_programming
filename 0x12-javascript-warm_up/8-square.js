#!/usr/bin/node
const size = parseInt(process.argv[2]);
let row = '';
for (let i = 0; i < size; i++) {
  row += 'X';
}
if (!size && size !== 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log(row);
  }
}
