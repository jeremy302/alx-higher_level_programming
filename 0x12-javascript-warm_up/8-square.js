#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(Number(arg));
if (isNaN(num)) { console.log('Missing size'); } else {
  for (let i = 0; i < num; i++) { console.log('X'.repeat(num)); }
}
