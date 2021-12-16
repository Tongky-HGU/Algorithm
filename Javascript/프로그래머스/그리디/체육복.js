function solution(n, lost, reserve) {
  const cloth = new Array(n + 1).fill(1);
  cloth[0] = 0;
  reserve.forEach((x) => (cloth[x] = 2));
  lost.forEach((x) => (cloth[x] -= 1));

  for (let i = 1; i < n + 1; i++) {
    if (cloth[i] === 0) {
      if (cloth[i - 1] === 2) {
        cloth[i - 1] = 1;
        cloth[i] = 1;
      } else if (cloth[i + 1] === 2) {
        cloth[i + 1] = 1;
        cloth[i] = 1;
      }
    }
  }

  return cloth.filter((x) => x >= 1).length;
}
