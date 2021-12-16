function solution(people, limit) {
  let ans = 0;
  let cl = 0;
  let cr = people.length - 1;

  people.sort((a, b) => a - b);

  while (cl <= cr) {
    if (people[cl] + people[cr] <= limit) {
      cl += 1;
      cr -= 1;
      ans += 1;
    } else {
      cr -= 1;
      ans += 1;
    }
  }

  return ans;
}
