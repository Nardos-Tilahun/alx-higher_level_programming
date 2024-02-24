#!/usr/bin/node
const { dict } = require('./101-data');

// Function to invert the dictionary
function invertDictionary (dict) {
  const invertedDict = {};
  for (const userId in dict) {
    const occurrences = dict[userId];
    if (!invertedDict[occurrences]) {
      invertedDict[occurrences] = [];
    }
    invertedDict[occurrences].push(userId);
  }
  return invertedDict;
}

// Compute the inverted dictionary
const invertedDict = invertDictionary(dict);

// Print the inverted dictionary
console.log(invertedDict);
