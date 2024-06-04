#!/usr/bin/node
/* Script that displays the status code of a GET request */
const request = require('request');

const url = process.argv[2];

const options = {
  url,
  method: 'GET'
};

request(options, function (error, response) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
