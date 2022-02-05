// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const A = input[0];
let ans = 1;

for (let i = 0; i < A.length; i++) {
  if (i === 0 || A[i] !== A[i - 1]) {
    if (A[i] === "d") {
      ans = ans * 10;
    } else {
      ans = ans * 26;
    }
  } else {
    if (A[i] === "d") {
      ans = ans * 9;
    } else {
      ans = ans * 25;
    }
  }
}

console.log(ans);
