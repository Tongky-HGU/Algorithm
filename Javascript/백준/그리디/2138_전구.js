// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const A = input[1]
  .trim()
  .split("")
  .map((x) => Boolean(Number(x)));
const B = input[2]
  .trim()
  .split("")
  .map((x) => Boolean(Number(x)));
let ans = -1;

const click = (A, i) => {
  A[i - 1] = !A[i - 1];
  A[i] = !A[i];
  if (i + 1 < A.length) A[i + 1] = !A[i + 1];
};

const solve = (A, firstClicked) => {
  let cnt = 0;

  if (firstClicked) {
    A[0] = !A[0];
    A[1] = !A[1];
    cnt += 1;
  }

  for (let i = 0; i < A.length; i++) {
    if (A[i] !== B[i]) {
      cnt += 1;
      if (i < A.length - 1) click(A, i + 1);
      else {
        return;
      }
    }
  }
  ans = Math.min(cnt);
};

solve([...A], true);
solve([...A], false);

console.log(ans);
