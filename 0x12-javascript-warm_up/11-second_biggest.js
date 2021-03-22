#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const copy = process.argv.slice(2, process.argv.length);
  copy.map(Number).sort((a, b) => a - b);
  console.log(copy[copy.length - 2]);
}
