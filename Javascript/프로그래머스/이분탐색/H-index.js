function solution(citations) {
  let ans = 0;
  let cr = Math.max(...citations);
  let cl = 0;
  const N = citations.length;

  while (cl <= cr) {
    const mid = Math.floor((cl + cr) / 2);
    const H = citations.filter((x) => x >= mid).length;

    if (H >= mid) {
      ans = mid;
      cl = mid + 1;
    } else {
      cr = mid - 1;
    }
  }

  return ans;
}
