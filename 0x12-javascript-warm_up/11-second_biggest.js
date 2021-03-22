#!/usr/bin/node
let idx = 0;

function biggest (arr) {
  let biggest = 0;
  let indx = 0;
  arr.forEach((val, index) => {
    if (val > biggest) {
      biggest = val;
      indx = index;
    }
  });
  return (indx);
}
let copy = process.argv.slice();
if (copy.length <= 3) {
  console.log(0);
} else {
  idx = biggest(copy);
  copy.splice(idx, 1);
  idx = biggest(copy);
  console.log(copy[idx]);
}
