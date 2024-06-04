#!/usr/bin/node
/* Script that writes a string to a file. */
const fs = require('fs');

const filePath = process.argv[2];
const text = process.argv[3];

try {
  fs.writeFileSync(filePath, text, 'utf-8');
} catch (err) {
  console.error(`Error writing text: ${err.message}`);
  process.exit(1);
}
