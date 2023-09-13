#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      let row = '';
      for (let i = 0; i < this.width; i++) row += c;
      for (let i = 0; i < this.height; i++) console.log(row);
    }
  }
}
module.exports = Square;
