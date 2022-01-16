// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const A = input[1].trim().split(" ");
const M = input[2].split(" ");
const B = input[3].trim().split(" ");

const cnt = {};

A.forEach((x) => (cnt[x] ? (cnt[x] += 1) : (cnt[x] = 1)));

const ans = B.map((x) => cnt[x] ?? 0);

console.log(ans.join(" "));
