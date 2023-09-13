#!/usr/bin/node
exports.logMe = function (item) {
  this.calls = this.calls ? this.calls + 1 : 1;
  console.log((this.calls - 1) + ': ' + item);
};
