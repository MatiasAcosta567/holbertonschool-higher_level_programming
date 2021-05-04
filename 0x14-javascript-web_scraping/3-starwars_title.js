#!/usr/bin/node
const api = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');

request(api, function (err, res, body) {
  if (!err) {
    console.log(JSON.parse(body).title);
  }
});
