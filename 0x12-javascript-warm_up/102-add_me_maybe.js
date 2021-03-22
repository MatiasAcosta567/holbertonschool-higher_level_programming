#!/usr/local/bin/node
function addMeMaybe (number, func) {
  number += 1;
  func(number);
}

module.exports.addMeMaybe = addMeMaybe;
