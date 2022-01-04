// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const [N, K] = input[0].split(" ").map((x) => Number(x));
const MOD = 1000000000;
const dp = Array.from(new Array(K + 1), () => new Array(N + 1).fill(0));

for (let i = 1; i <= K; i++) {
  dp[i][0] = 1;
  for (let j = 1; j <= N; j++) {
    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD;
  }
}

console.log(dp[K][N]);
