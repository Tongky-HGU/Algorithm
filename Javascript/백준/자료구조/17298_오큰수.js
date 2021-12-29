// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map((x) => Number(x));

const ans = new Array(N).fill(-1);
const stack = [];

for (let i = 0; i < N; i++) {
  while (stack.length && A[stack[stack.length - 1]] < A[i]) {
    ans[stack.pop()] = A[i];
  }
  stack.push(i);
}

console.log(ans.join(" "));
