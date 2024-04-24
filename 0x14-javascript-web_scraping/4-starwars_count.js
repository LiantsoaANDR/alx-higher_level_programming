#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, data, body) {
  if (err) {
    console.log(err);
    return;
  }

  let count = 0;
  const films = JSON.parse(body).results;

  for (let i = 0; i < films.length; i++) {
    const characList = films[i].characters;
    for (let j = 0; j < characList.length; j++) {
      const charac = characList[j];
      const ID = charac.split('/')[5];
      if (ID === '18') {
        count++;
      }
    }
  }

  console.log(count);
});
