// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const A = [];

for (let i = 1; i < N + 1; i++) {
  const num = BigInt(input[i].trim());
  A.push(num);
}

A.sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));

let temp = Infinity;
let cnt = 0;
let max = 0;
let ans = null;

for (let i = 0; i < N; i++) {
  if (A[i] === temp) {
    cnt += 1;
  } else {
    temp = A[i];
    cnt = 1;
  }
  if (cnt > max) {
    ans = A[i];
    max = cnt;
  }
}

console.log(ans.toString());
