function solution(routes) {
  const ROAD_START = -30000;
  let ans = 0;
  let camera = ROAD_START - 1;
  routes.sort((a, b) => a[1] - b[1]);
  routes.forEach((route) => {
    if (route[0] > camera) {
      ans += 1;
      camera = route[1];
    }
  });
  return ans;
}
