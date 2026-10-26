#!/usr/bin/node

const args = process.argv.slice(2);
const size = args.length;

if (size <= 1) {
  console.log(0);
} else {
  const numbers = args.map(function (t) {
    return parseInt(t);
  });
  numbers.sort(function (a, b) {
    return b - a;
  });
  console.log(numbers[1]);
}
