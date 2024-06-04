#!/usr/bin/node
/* Script that computes the number of tasks completed by user id */
const request = require('request');
const url = process.argv[2];

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
    const completedTasks = {};

    body.forEach(task => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId]++;
      }
    });

    console.log(completedTasks);
  }
});
