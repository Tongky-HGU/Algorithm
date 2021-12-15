function solution(answers) {
  const score = { 1: 0, 2: 0, 3: 0 };
  const N = answers.length;

  let ansA = 0;
  let ansB = 0;
  let ansC = 0;
  const cPattern = [null, 3, 1, 2, 4, 5];

  for (let i = 0; i < N; i++) {
    const checkAnswer = (who, ans) => {
      if (ans === answers[i]) {
        score[who] += 1;
      }
    };
    // 1
    ansA = ansA === 5 ? 1 : ansA + 1;
    checkAnswer("1", ansA);

    // 2
    if (i % 2 === 0) {
      checkAnswer("2", 2);
    } else {
      ansB = ansB === 5 ? 1 : ansB + 1;
      ansB = ansB === 2 ? 3 : ansB;
      checkAnswer("2", ansB);
    }

    // 3
    if (i % 2 === 0) {
      ansC = ansC === 5 ? 1 : ansC + 1;
      checkAnswer("3", cPattern[ansC]);
    } else {
      checkAnswer("3", cPattern[ansC]);
    }
  }

  const maxScore = Math.max(...Object.values(score));
  return Object.keys(score)
    .filter((x) => score[x] === maxScore)
    .map((x) => Number(x));
}
