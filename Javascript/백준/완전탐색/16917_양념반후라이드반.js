// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const [A, B, C, X, Y] = input[0]
  .trim()
  .split(" ")
  .map((x) => Number(x));
let ans = 0;

if (2 * C > A + B) {
  ans = A * X + B * Y;
} else {
  const d = Math.min(X, Y);
  ans =
    2 * C * d +
    Math.min(2 * C, A) * Math.max(0, X - d) +
    Math.min(2 * C, B) * Math.max(0, Y - d);
}

console.log(ans);
