#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let square = '';
    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        square += c != undefined ? c : 'X';
      }
      if (y < this.height - 1) {
        square += '\n';
      }
    }
    console.log(square);
  }
}

module.exports = Square;
