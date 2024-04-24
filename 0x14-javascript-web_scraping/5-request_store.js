#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2], function (err, data, body) {
  if (err) {
    console.log(err);
    return;
  }

  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
