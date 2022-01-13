// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const solution = () => {
  const [N, M] = input[0].split(" ").map((x) => Number(x));
  const A = new Array(N);
  let ans = 0;

  for (let i = 0; i < N; i++) {
    const a = input[i + 1].trim().split("");
    const b = input[i + N + 1].trim().split("");
    A[i] = [];
    a.forEach((x, idx) => A[i].push(x === b[idx]));
  }

  if (N < 3 || M < 3) {
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        if (!A[i][j]) {
          console.log(-1);
          return;
        }
      }
    }
    console.log(0);
    return;
  }

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (!A[i][j]) {
        ans += 1;
        if (i < N - 2 && j < M - 2) {
          for (let k = i; k < i + 3; k++) {
            for (let l = j; l < j + 3; l++) {
              A[k][l] = !A[k][l];
            }
          }
        } else {
          console.log(-1);
          return;
        }
      }
    }
  }

  console.log(ans);
};

solution();
