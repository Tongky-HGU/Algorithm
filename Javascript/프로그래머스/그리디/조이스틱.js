function solution(name) {
  let ans = 0;
  const alpha = name.split("");
  const A = "A".charCodeAt();
  const Z = "Z".charCodeAt();

  let shift = alpha.length - 1;
  alpha.forEach((x, i) => {
    if (x === "A") {
      let nextA = i;
      while (alpha[nextA] === "A") {
        nextA += 1;
      }
      const left = i === 0 ? 0 : i - 1;
      const right = alpha.length - nextA;
      shift = Math.min(shift, left + right + Math.min(left, right));
    }
  });

  ans += shift;

  alpha.forEach((x) => {
    const X = x.charCodeAt();
    ans += Math.min(X - A, Z - X + 1);
  });

  return ans;
}
