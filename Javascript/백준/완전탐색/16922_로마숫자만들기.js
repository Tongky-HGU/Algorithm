// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const A = [1, 5, 10, 50];
const visit = new Array(50 * N + 1).fill(false);
let ans = 0;

const dfs = (num, idx, cnt) => {
  if (cnt === N) {
    if (!visit[num]) {
      ans += 1;
      visit[num] = true;
    }
    return;
  }

  for (let i = idx; i < A.length; i++) {
    dfs(num + A[i], i, cnt + 1);
  }
};

dfs(0, 0, 0);

console.log(ans);
