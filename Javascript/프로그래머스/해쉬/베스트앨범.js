function solution(genres, plays) {
  const ans = [];
  const allGenreMap = {};
  const allGenrePlays = {};

  genres.forEach((genre, idx) => {
    allGenreMap[genre] = allGenreMap[genre] ? allGenreMap[genre] : [];
    allGenreMap[genre].push(idx);
  });

  const allGenre = Object.keys(allGenreMap);
  allGenre.forEach((genre) => {
    allGenrePlays[genre] = allGenreMap[genre]
      .map((id) => plays[id])
      .reduce((p, x) => p + x);
  });

  allGenre.sort((a, b) => allGenrePlays[b] - allGenrePlays[a]);

  allGenre.forEach((genre) => {
    allGenreMap[genre].sort((a, b) =>
      plays[a] === plays[b] ? a - b : plays[b] - plays[a]
    );
    ans.push(allGenreMap[genre][0]);
    if (allGenreMap[genre][1] !== undefined) {
      ans.push(allGenreMap[genre][1]);
    }
  });

  return ans;
}
