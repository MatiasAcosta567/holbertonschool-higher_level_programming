#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, res, body) {
  if (!err) {
    fs.writeFile(process.argv[3], body, function (error) {
      if (error) {
        return console.log(error);
      }
    });
  }
});
