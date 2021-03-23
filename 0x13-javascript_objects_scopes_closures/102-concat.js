#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const fs = require('fs');

let data = fs.readFileSync(fileA,
  { encoding: 'utf8', flag: 'r' });

data += fs.readFileSync(fileB,
  { encoding: 'utf8', flag: 'r' });

fs.writeFileSync(fileC, data);
