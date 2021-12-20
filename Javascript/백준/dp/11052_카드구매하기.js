// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map((x) => Number(x));

const dp = new Array(N + 1).fill(0);

A.forEach((price, idx) => (dp[idx + 1] = price));

for (let i = 1; i <= N; i++) {
  for (let j = 1; j <= i; j++) {
    const divide = Math.floor(i / j);
    const rest = i % j;
    dp[i] = Math.max(dp[i], dp[j] * divide + dp[rest]);
  }
}

console.log(dp[N]);
