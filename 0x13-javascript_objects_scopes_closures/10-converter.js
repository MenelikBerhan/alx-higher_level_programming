#!/usr/bin/node
exports.converter = function (base) {
  this.base = base;
  function convert (num) {
    return num.toString(this.base);
  }
  return convert;
};
