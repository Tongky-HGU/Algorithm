function solution(v) {
  const xMap = {};
  const yMap = {};

  v.forEach((point) => {
    const [x, y] = point;

    if (xMap[x]) delete xMap[x];
    else xMap[x] = true;

    if (yMap[y]) delete yMap[y];
    else yMap[y] = true;
  });

  return [Number(...Object.keys(xMap)), Number(...Object.keys(yMap))];
}
