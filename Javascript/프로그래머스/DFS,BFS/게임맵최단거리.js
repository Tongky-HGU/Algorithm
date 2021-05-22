// 게임맵최단거리
function solution(maps) {
  let ans = -1;
  const N = maps.length;
  const M = maps[0].length;

  let vis = Array.from(Array(N), () => new Array(M).fill(0));

  const dr = [1, 0, -1, 0];
  const dc = [0, -1, 0, 1];

  const stack = [[0, 0, 1]];
  vis[0][0] = 1;

  while (stack.length) {
    let [r, c, cnt] = stack.shift();
    // console.log(r,c,cnt)
    if (r == N - 1 && c == M - 1) {
      return cnt;
    }
    for (let i = 0; i < 4; i++) {
      let nr = r + dr[i];
      let nc = c + dc[i];

      if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
      if (vis[nr][nc]) continue;
      if (!maps[nr][nc]) continue;

      vis[nr][nc] = 1;
      stack.push([nr, nc, cnt + 1]);
    }
  }

  return ans;
}
