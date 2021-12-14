function solution(participant, completion) {
  const completedMap = {};

  participant.forEach((name) => {
    completedMap[name] = completedMap[name] ? completedMap[name] : 0;
    completedMap[name] += 1;
  });
  completion.forEach((name) => (completedMap[name] -= 1));

  return Object.keys(completedMap).filter(
    (name) => completedMap[name] !== 0
  )[0];
}

[1].reduce();
