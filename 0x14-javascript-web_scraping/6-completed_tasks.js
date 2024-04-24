#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }
  const completedTask = {};
  const data = JSON.parse(body);

  for (let i = 0; i < data.length; i++) {
    if (data[i].completed) {
      if (completedTask[data[i].userId]) {
        completedTask[data[i].userId]++;
      } else {
        completedTask[data[i].userId] = 1;
      }
    }
  }

  console.log(completedTask);
});
