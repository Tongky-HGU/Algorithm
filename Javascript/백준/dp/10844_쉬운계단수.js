// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const dp = Array.from(new Array(N + 1), () => new Array(10).fill(0));
const MOD = 1000000000;

dp[1] = new Array(10).fill(1);

for (let i = 2; i <= N; i++) {
  for (let j = 0; j < 10; j++) {
    if (j - 1 >= 0) {
      dp[i][j] += dp[i - 1][j - 1];
    }
    if (j + 1 <= 9) {
      dp[i][j] += dp[i - 1][j + 1];
    }
    dp[i][j] = dp[i][j] % MOD;
  }
}

console.log((dp[N].reduce((a, b) => a + b) - dp[N][0]) % MOD);
