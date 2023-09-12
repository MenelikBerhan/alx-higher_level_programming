#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let biggest;
  let secondBiggest;
  if (process.argv[2] > process.argv[3]) {
    biggest = parseInt(process.argv[2]);
    secondBiggest = parseInt(process.argv[3]);
  } else {
    biggest = parseInt(process.argv[3]);
    secondBiggest = parseInt(process.argv[2]);
  }
  for (let i = 4; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) >= biggest) {
      secondBiggest = biggest;
      biggest = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) > secondBiggest) {
      secondBiggest = parseInt(process.argv[i]);
    }
  }
  console.log(secondBiggest);
}
