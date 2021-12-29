// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map((x) => Number(x));

const stack = [];
const ans = new Array(N).fill(-1);
const cnt = {};

A.forEach((x) => (cnt[x] ? (cnt[x] += 1) : (cnt[x] = 1)));

for (let i = 0; i < N; i++) {
  while (stack.length && cnt[A[i]] > cnt[A[stack[stack.length - 1]]]) {
    ans[stack.pop()] = A[i];
  }
  stack.push(i);
}

console.log(ans.join(" "));
