// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = input[0];
const dp = Array.from(new Array(100001), () => new Array(4).fill(0));

dp[1][1] = 1;
dp[2][2] = 1;
dp[3][1] = 1;
dp[3][2] = 1;
dp[3][3] = 1;

for (let i = 4; i <= 100000; i++) {
  dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % 1000000009;
  dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % 1000000009;
  dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % 1000000009;
}

for (let i = 1; i <= N; i++) {
  console.log(dp[Number(input[i])].reduce((a, b) => a + b) % 1000000009);
}
