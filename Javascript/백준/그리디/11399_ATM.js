// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map((x) => Number(x));
let ans = 0;
A.sort((a, b) => a - b);

A.reduce((p, x) => {
  ans += p + x;
  return p + x;
}, 0);

console.log(ans);
