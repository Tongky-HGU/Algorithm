function solution(rows, columns, queries) {
  const ans = [];
  const map = Array.from(Array(rows), () => new Array(columns));

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < columns; c++) {
      map[r][c] = r * columns + c + 1;
    }
  }

  queries.forEach(([x1, y1, x2, y2]) => {
    let min = Infinity;
    let prevNum = Infinity;

    const moveAndCheckIsMinimum = (r, c) => {
      const temp = map[r][c];
      min = Math.min(min, map[r][c]);
      map[r][c] = prevNum;
      prevNum = temp;
    };

    for (let c = y1 - 1; c < y2; c++) {
      moveAndCheckIsMinimum(x1 - 1, c);
    }

    for (let r = x1; r < x2; r++) {
      moveAndCheckIsMinimum(r, y2 - 1);
    }

    for (let c = y2 - 2; c > y1 - 2; c--) {
      moveAndCheckIsMinimum(x2 - 1, c);
    }

    for (let r = x2 - 2; r > x1 - 2; r--) {
      moveAndCheckIsMinimum(r, y1 - 1);
    }
    ans.push(min);
  });

  return ans;
}
