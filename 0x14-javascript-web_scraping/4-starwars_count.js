#!/usr/bin/node
const request = require('request');
let total = 0;
request(process.argv[2], function (err, res, body) {
  if (!err) {
    const films = JSON.parse(body).results;
    films.forEach(film => {
      film.characters.forEach(elem => {
        if (elem.endsWith('/18/')) {
          total++;
        }
      });
    });
    return console.log(total);
  }
});
