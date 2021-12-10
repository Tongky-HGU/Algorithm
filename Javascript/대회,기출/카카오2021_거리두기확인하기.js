function checkPosition(place) {
  const R = place.length;
  const C = place[0].length;
  const dr = [0, 1, 0, -1];
  const dc = [1, 0, -1, 0];

  for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
      if (place[i][j] === "X") continue;
      let cnt = place[i][j] === "P" ? 1 : 0;
      for (let k = 0; k < 4; k++) {
        const cr = i + dr[k];
        const cc = j + dc[k];
        if (cr < 0 || cr >= R || cc < 0 || cc >= C) continue;
        if (place[cr][cc] === "P") cnt += 1;
      }
      if (cnt > 1) return 0;
    }
  }
  return 1;
}

function solution(places) {
  const ans = [];

  places.forEach((place) => ans.push(checkPosition(place)));
  return ans;
}
