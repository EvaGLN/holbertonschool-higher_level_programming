#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2]);

if (Number.isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let t = 0; t <= x; t++) {
    console.log('C is fun');
  }
}
