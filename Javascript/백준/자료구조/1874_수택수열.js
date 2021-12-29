// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const number = [];
const sorted = [];
const stack = [];
let ans = [];

for (let i = 1; i <= N; i++) {
  number.push(Number(input[i].trim()));
  sorted.push(i);
}

while (number.length) {
  const target = number.shift();

  while (
    sorted.length &&
    target >= sorted[0] &&
    stack[stack.length - 1] !== target
  ) {
    stack.push(sorted.shift());
    ans.push("+");
  }

  if (stack[stack.length - 1] === target) {
    stack.pop();
    ans.push("-");
  } else {
    ans.push("NO");
    break;
  }
}

if (ans[ans.length - 1] === "NO") console.log("NO");
else console.log(ans.join("\n"));
