// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);

for (let i = 1; i <= N; i++) {
  const data = input[i].trim().split(" ");
  const ans = data.map((word) => word.split("").reverse().join("")).join(" ");
  console.log(ans);
}
