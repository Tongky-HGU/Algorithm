function solution(cacheSize, cities) {
  let ans = 0;
  const cache = [];

  cities.forEach((inputCity) => {
    const city = inputCity.toUpperCase();
    const idx = cache.findIndex((x) => x === city);
    if (idx === -1) {
      ans += 5;
      if (cache.length === cacheSize) {
        cache.shift();
      }
    } else {
      ans += 1;
      cache.splice(idx, 1);
    }

    if (cache.length < cacheSize) {
      cache.push(city);
    }
  });
  return ans;
}
