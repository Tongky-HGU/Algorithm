// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

let [N, M] = input[0]
  .trim()
  .split(" ")
  .map((x) => Number(x));

let ans = 0;
let i = 1;
let nine = 9;

while (M > i * nine) {
  M = M - i * nine;
  ans = ans + nine;
  i += 1;
  nine = nine * 10;
}

ans = ans + 1 + Math.floor((M - 1) / i);

console.log(ans > N ? "-1" : String(ans)[(M - 1) % i]);
