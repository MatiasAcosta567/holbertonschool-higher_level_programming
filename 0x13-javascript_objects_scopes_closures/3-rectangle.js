#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect = '';
    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        rect += 'X';
      }
      if (y < this.height - 1) {
        rect += '\n';
      }
    }
    console.log(rect);
  }
}

module.exports = Rectangle;
