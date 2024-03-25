#!/usr/bin/node
const args = process.argv;
args[2] === undefined ? console.log('No argument') : console.log(args[2]);
