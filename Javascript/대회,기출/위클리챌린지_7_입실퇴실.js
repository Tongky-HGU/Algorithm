function solution(enter, leave) {
  const N = enter.length;
  const ans = new Array(N).fill(0);
  const room = [];
  enter.reverse();

  for (let out of leave) {
    if (room.includes(out)) {
      const idx = room.findIndex(x => x === out);
      room.splice(idx, idx + 1);
    } else {
        while (enter[enter.length - 1] !== out) {
          room.push(enter.pop());
        }
      enter.pop();
    }
    ans[out - 1] += room.length;
    room.forEach(x => (ans[x - 1] += 1));
  }
  return ans;
}

// console.log(solution([1, 3, 2], [1, 2, 3]));
console.log(solution([1, 2,3,4,6,5], [1,2,3,4,5,6]));
