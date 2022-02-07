// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const [N, M] = input[0].split(" ").map((x) => Number(x));
const [A, B] = input[M + 1].split(" ").map((x) => Number(x));
const road = Array.from(Array(N + 1), (x) => []);
let min = Infinity;
let max = 0;

for (let i = 0; i < M; i++) {
  const [a, b, d] = input[i + 1]
    .trim()
    .split(" ")
    .map((x) => Number(x));
  road[a].push([b, d]);
  road[b].push([a, d]);
  min = Math.min(min, d);
  max = Math.max(max, d);
}

const search = (weight) => {
  const visit = new Array(N + 1).fill(false);
  let ans = false;

  const dfs = (a) => {
    if (visit[a]) return;
    visit[a] = true;
    if (a === B) {
      ans = true;
      return;
    }
    road[a].forEach(([b, d]) => {
      if (weight > d) return;
      dfs(b);
    });
  };

  dfs(A);
  return ans;
};

let cl = min;
let cr = max;
let ans = 0;

while (cl <= cr) {
  const mid = Math.floor((cl + cr) / 2);

  if (search(mid)) {
    ans = Math.max(mid, ans);
    cl = mid + 1;
  } else {
    cr = mid - 1;
  }
}

console.log(ans);
