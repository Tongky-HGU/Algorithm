// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);

const dp = Array.from(new Array(N + 1), () => new Array(2).fill(BigInt(0)));
dp[1][1] = BigInt(1);

for (let i = 2; i <= N; i++) {
  dp[i][0] = dp[i - 1][0] + dp[i - 1][1];
  dp[i][1] = dp[i - 1][0];
}

console.log(dp[N].reduce((a, b) => a + b).toString());

// const dp = new Array(N + 1).fill(BigInt(0));

// dp[1] = BigInt(1);

// for (let i = 2; i <= N; i++) {
//   dp[i] = dp[i - 1] + dp[i - 2];
// }
// console.log(dp[N].toString());
