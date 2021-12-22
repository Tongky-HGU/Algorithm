// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const N = Number(input[0]);
const A = input[1]
  .trim()
  .split(" ")
  .map((x) => Number(x));

const dp = new Array(N).fill(0);
const lis = Array.from(new Array(N), (_, i) => [A[i]]);

for (let i = 1; i < N; i++) {
  for (let j = 0; j < i; j++) {
    if (A[i] > A[j] && dp[j] + 1 > dp[i]) {
      dp[i] = dp[j] + 1;
      lis[i] = [...lis[j], A[i]];
    }
  }
}

const max = Math.max(...dp);
const maxIndex = dp.findIndex((x) => x === max);

console.log(lis[maxIndex].length);
console.log(lis[maxIndex].join(" "));

// const stack = [];

// A.forEach((x) => {
//   if (stack.length === 0 || x > stack[stack.length - 1]) {
//     stack.push(x);
//   } else if (x < stack[stack.length - 1]) {
//     let cl = 0;
//     let cr = stack.length - 1;
//     let mid = 0;

//     while (cl <= cr) {
//       mid = Math.floor((cl + cr) / 2);
//       if (x === stack[mid] || x < stack[0]) {
//         break;
//       }
//       if (x > stack[mid]) {
//         cl = mid + 1;
//       } else {
//         cr = mid - 1;
//       }
//     }

//     stack[mid] = x;
//   }
//   console.log(stack);
// });

// console.log(stack.length);
// console.log(stack.join(" "));
