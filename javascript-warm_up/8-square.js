#!/usr/bin/node

const args = process.argv;
const size = parseInt(args[2]);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let line = 1; line <= size; line++) {
    let row = '';
    for (let column = 1; column <= size; column++) {
      row += 'X';
    }
    console.log(row);
  }
}
