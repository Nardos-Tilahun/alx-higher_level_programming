#!/usr/bin/node
const argv = process.argv;
if (argv.slice(2).length === 0) {
  console.log('No argument');
} else {
  console.log('Argument Found');
}
