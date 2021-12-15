const permutations = (array, n) => {
  const result = [];
  if (n === 1) {
    return array.map((x) => [x]);
  }
  array.forEach((x, idx, origin) => {
    const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
    const combis = permutations(rest, n - 1);
    const attach = combis.map((combi) => [x, ...combi]);
    result.push(...attach);
  });
  return result;
};

const isAlone = (n) => {
  if (n === 0 || n === 1) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
};

const solution = (input) => {
  const numbers = input.split("");
  const combis = new Set();

  for (let i = 1; i <= numbers.length; i++) {
    const result = permutations(numbers, i);
    result.map((x) => Number(x.join(""))).forEach((x) => combis.add(x));
  }

  return [...combis].filter((x) => isAlone(x)).length;
};
