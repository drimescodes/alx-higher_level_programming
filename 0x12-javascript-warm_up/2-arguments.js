#!/usr/bin/node
const args = process.argv;
args.length === 2
  ? console.log('No argument')
  : args.length === 3
    ? console.log('Argument found')
    : console.log('Arguments found');
