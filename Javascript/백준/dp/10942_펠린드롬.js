// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map((x) => Number(x));
const M = Number(input[2]);
const questions = [];
const dp = Array.from(new Array(N), () => new Array(N).fill(0));

for (let i = 0; i < M; i++) {
  questions.push(input[i + 3].split(" ").map((x) => Number(x)));
}

for (let length = 0; length < N; length++) {
  for (let cl = 0; cl < N; cl++) {
    const cr = cl + length;
    if (cl === cr) {
      dp[cl][cr] = 1;
    } else if (A[cl] === A[cr]) {
      if (cr - cl === 1) dp[cl][cr] = 1;
      else if (dp[cl + 1][cr - 1]) dp[cl][cr] = 1;
    }
  }
}

const ans = [];

for (let i = 0; i < M; i++) {
  const [cl, cr] = questions[i];
  ans.push(dp[cl - 1][cr - 1]);
}

console.log(ans.join("\n"));
