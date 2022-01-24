// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const A = [];

for (let i = 0; i < N; i++) {
  const x = input[i + 1].split(" ").map((x) => Number(x));
  A.push(x);
}

A.sort((a, b) => {
  if (a[1] === b[1]) return a[0] - b[0];
  return a[1] - b[1];
});

const ans = A.map((x) => x.join(" "));

console.log(ans.join("\n"));
