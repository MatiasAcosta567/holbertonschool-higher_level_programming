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
if (process.argv.length <= 3) {
  console.log(0);
} else {
  idx = biggest(process.argv);
  process.argv.splice(idx, 1);
  idx = biggest(process.argv);
  console.log(process.argv[idx]);
}
