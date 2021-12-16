function solution(brown, yellow) {
  const ans = [];
  for (let r = 3; r <= brown; r++) {
    for (let c = 3; c <= r; c++) {
      if (r * c !== brown + yellow) continue;
      if ((r - 2) * (c - 2) !== yellow) continue;
      return [r, c];
    }
  }
}
