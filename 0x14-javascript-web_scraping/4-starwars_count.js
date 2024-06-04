#!/usr/bin/node
/* script that prints the number of movies where the character “Wedge Antilles” is present */
const request = require('request');

const url = process.argv[2];

const options = {
  url,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Unexpected status code ${response.statusCode}`);
    process.exit(1);
  } else {
    const films = body.results;
    const characterID = 'https://swapi-api.alx-tools.com/api/people/18/';
    let count = 0;

    films.forEach(film => {
      if (film.characters.includes(characterID)) {
        count++;
      }
    });

    console.log(count);
  }
});
