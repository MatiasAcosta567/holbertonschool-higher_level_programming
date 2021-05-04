#!/usr/bin/node
const request = require('request');
const tasks = {};

request(process.argv[2], function (err, res, body) {
  if (!err) {
    const all = JSON.parse(body);
    all.forEach(element => {
      if (element.completed === true) {
        if (Object.prototype.hasOwnProperty.call(tasks, element.userId)) {
          tasks[element.userId] += 1;
        } else {
          tasks[element.userId] = 1;
        }
      }
    });
  }
  return console.log(tasks);
});
