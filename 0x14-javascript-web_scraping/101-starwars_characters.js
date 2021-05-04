#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(api, function (err, res, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printChar(characters, 0);
  }
});

function printChar (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printChar(characters, index + 1);
      }
    }
  });
}
