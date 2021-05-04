#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(api, function (err, res, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    characters.forEach(element => {
      request(element, function (err, res, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
