// const line = require("fs").readFileSync("/dev/stdin", "utf8");
const line = require("fs").readFileSync("./input.txt", "utf8");

const input = line.trim().split("\n");

const N = Number(input[0]);
const A = [];

for (let i = 0; i < N; i++) {
  const [age, name] = input[i + 1].trim().split(" ");
  A.push({ name, age, i });
}

A.sort((a, b) => {
  if (a.age === b.age) return a.name - b.name;
  return a.age - b.age;
});

const ans = A.map((x) => `${x.age} ${x.name}`);

console.log(ans.join("\n"));
