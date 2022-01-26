// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const A = [];

const compareAscii = (a, b) => {
  for (let i = 0; i < 10; i++) {
    if (a[i] !== b[i]) return a[i].charCodeAt() - b[i].charCodeAt();
  }
};

for (let i = 0; i < N; i++) {
  const score = input[i + 1].trim().split(" ");
  A.push({ name: score[0], a: score[1], b: score[2], c: score[3] });
}

A.sort((a, b) => {
  if (a.a !== b.a) return b.a - a.a;
  if (a.b !== b.b) return a.b - b.b;
  if (a.c !== b.c) return b.c - a.c;
  return compareAscii(a.name, b.name);
});

const ans = A.map((x) => x.name);

console.log(ans.join("\n"));
