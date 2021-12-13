const getRound = (n) => {
  let round = 0;
  while (n > 1) {
    n = n / 2;
    round += 1;
  }
  return round;
};

function solution(n, a, b) {
  let round = getRound(n);
  let cl = 1;
  let cr = n;

  const left = a < b ? a : b;
  const right = a < b ? b : a;

  while (cl < cr) {
    const mid = (cl + cr) / 2;

    if (left <= mid && right > mid) {
      return round;
    } else if (left <= mid && right < mid) {
      cr = mid - 1;
    } else {
      cl = mid + 1;
    }
    round -= 1;
  }
  return round;
}
