#!/usr/bin/node
const argv = process.argv;
if (argv.length > 3) {
  console.log(
    argv
      .slice(2)
      .map((x) => Number(x))
      .sort((a, b) => b - a)[1]
  );
} else console.log(0);
