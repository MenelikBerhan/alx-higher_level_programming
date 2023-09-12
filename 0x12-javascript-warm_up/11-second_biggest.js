#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let biggest;
  let secondBiggest;
  if (process.argv[2] > process.argv[3]) {
    biggest = process.argv[2];
    secondBiggest = process.argv[3];
  } else {
    biggest = process.argv[3];
    secondBiggest = process.argv[2];
  }
  for (let i = 4; i < process.argv.length; i++) {
    if (process.argv[i] >= biggest) {
      secondBiggest = biggest;
      biggest = process.argv[i];
    } else if (process.argv[i] > secondBiggest) {
      secondBiggest = process.argv[i];
    }
  }
  console.log(secondBiggest);
}
