#!/usr/bin/node
/* Script that prints the title of a Star Wars movie where the episode number matches a given integer. */
const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

const options = {
  url,
  method: 'GET',
  json: true
};

request(options, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Unexpected status code ${response.statusCode}`);
    process.exit(1);
  } else {
    const title = body.title;
    console.log(title);
  }
});
