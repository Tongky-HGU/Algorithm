function solution(numbers, hand) {
  const ans = [];
  const comfort = hand === "right" ? "R" : "L";
  const key = {};
  "123456789*0#".split("").forEach((x, idx) => {
    const r = Math.floor(idx / 3);
    const c = idx % 3;
    key[x] = [r, c];
  });

  let L = "*";
  let R = "#";
  numbers.forEach((x) => {
    if ([1, 4, 7].includes(x)) {
      ans.push("L");
      L = x;
      return;
    }
    if ([3, 6, 9].includes(x)) {
      ans.push("R");
      R = x;
      return;
    }
    const dl =
      Math.abs(key[L][0] - key[x][0]) + Math.abs(key[L][1] - key[x][1]);
    const dr =
      Math.abs(key[R][0] - key[x][0]) + Math.abs(key[R][1] - key[x][1]);
    if (dl === dr) {
      ans.push(comfort);
      comfort === "R" ? (R = x) : (L = x);
      return;
    }
    ans.push(dr < dl ? "R" : "L");
    dr < dl ? (R = x) : (L = x);
  });

  return ans.join("");
}
