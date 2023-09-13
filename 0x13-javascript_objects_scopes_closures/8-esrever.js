#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  for (let i = 0; i < list.length; i++) {
    reverse[i] = list[list.length - 1 - i];
  }
  return reverse;
};
