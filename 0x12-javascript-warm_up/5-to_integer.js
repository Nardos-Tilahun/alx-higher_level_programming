#!/usr/bin/node

const firstArg = process.argv[2];

// Check if the argument can be converted to an integer using isNaN
if (!isNaN(Number(firstArg))) {
  console.log(`My number: ${parseInt (Number(firstArg))}`);
} else {
  console.log("Not a number");
}
