// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = input[0];

const dp = new Array(N).fill(0);

dp[0] = 1;
dp[1] = 3;

for (let i = 2; i < N; i++) {
  dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007;
}

console.log(dp[N - 1]);
