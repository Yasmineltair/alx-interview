#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, result, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  actualOrder(actors, 0);
});
const actualOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, result, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    actualOrder(actors, x + 1);
  });
};
