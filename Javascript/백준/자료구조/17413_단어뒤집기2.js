// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");
const input = line.trim().split("\n");

const A = input[0].split("");
const ans = [];
let stack = [];
let flag = false;

A.forEach((x) => {
  switch (x) {
    case "<": {
      if (stack.length) {
        ans.push(stack.reverse().join(""));
        stack = [];
      }
      stack.push(x);
      flag = true;
      break;
    }
    case ">": {
      stack.push(x);
      ans.push(stack.join(""));
      stack = [];
      flag = false;
      break;
    }
    case " ": {
      if (flag) {
        stack.push(x);
      } else {
        stack.reverse();
        stack.push(x);
        ans.push(stack.join(""));
        stack = [];
      }
      break;
    }
    default: {
      stack.push(x);
    }
  }
});
if (stack.length) {
  ans.push(stack.reverse().join(""));
}

console.log(ans.join(""));
