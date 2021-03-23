#!/usr/bin/node
const dict = require('./101-data').dict;
const keys = Object.keys(dict);
const newDict = {};
for (const elem in keys) {
  console.log(dict[keys[elem]]);
  console.log(keys[elem]);
  if (newDict.hasOwnProperty(dict[keys[elem]])) {
    newDict[dict[keys[elem]]].push(keys[elem]);
  } else {
    newDict[dict[keys[elem]]] = [keys[elem]];
  }
}
console.log(newDict);
