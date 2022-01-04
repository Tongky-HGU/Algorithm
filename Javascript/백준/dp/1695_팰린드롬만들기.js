// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map((x) => Number(x));

const dp = Array.from(new Array(N), () => new Array(N).fill(-1));

const find = (cl, cr) => {
  if (cl >= cr) return 0;
  if (dp[cl][cr] !== -1) return dp[cl][cr];
  if (A[cl] === A[cr]) dp[cl][cr] = find(cl + 1, cr - 1);
  else dp[cl][cr] = Math.min(find(cl + 1, cr), find(cl, cr - 1)) + 1;
  return dp[cl][cr];
};

find(0, N - 1);
console.log(dp[0][N - 1]);
