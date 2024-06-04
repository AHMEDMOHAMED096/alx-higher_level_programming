#!/usr/bin/node
/* Script that gets the contents of a webpage and stores it in a file. */
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

const options = {
  url,
  method: 'GET',
};

request(options, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Unexpected status code ${response.statusCode}`);
    process.exit(1);
  } else {
    try {
      fs.writeFileSync(filePath, body, 'utf-8');
    } catch (err) {
      console.error(`Error writing text: ${err.message}`);
      process.exit(1);
    }
  }
});
