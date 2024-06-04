#!/usr/bin/node
/* Script that reads and prints the content of a file */
const fs = require('fs');

const filePath = process.argv[2];

try {
  const content = fs.readFileSync(filePath, 'utf-8');
  console.log(content);
} catch (err) {
  console.error(`Error reading file: ${err.message}`);
  process.exit(1);
}
