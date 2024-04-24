#!/usr/bin/node

const request = require('request');
const starURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(starURL, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const b = JSON.parse(body);
    console.log(b.title);
  }
});
