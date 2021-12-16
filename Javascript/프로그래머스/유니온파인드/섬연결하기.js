function solution(n, costs) {
  let ans = 0;
  const parent = [];

  const getParent = (x) => {
    if (x === parent[x]) return x;
    parent[x] = getParent(parent[x]);
    return parent[x];
  };
  const isSameParent = (a, b) => {
    const ca = getParent(a);
    const cb = getParent(b);
    return ca === cb ? true : false;
  };
  const union = (a, b) => {
    const ca = getParent(a);
    const cb = getParent(b);
    ca < cb ? (parent[ca] = cb) : (parent[cb] = ca);
  };

  for (let i = 0; i < n; i++) {
    parent.push(i);
  }

  costs.sort((a, b) => a[2] - b[2]);

  costs.forEach(([a, b, cost]) => {
    if (isSameParent(a, b)) return;
    union(a, b);
    ans += cost;
  });

  return ans;
}
