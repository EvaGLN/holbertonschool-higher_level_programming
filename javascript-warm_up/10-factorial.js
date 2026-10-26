#!/usr/bin/node

const args = process.argv;
const integer = parseInt(args[2]);

function factorial (n) {
  if (Number.isNaN(n) || n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(integer));
