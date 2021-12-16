function solution(number, k) {
  const numbers = number.split("").map((x) => Number(x));
  const stack = [];
  let deleted = 0;

  numbers.forEach((x) => {
    if (!stack.length || deleted === k) {
      stack.push(x);
      return;
    }

    while (stack[stack.length - 1] < x && deleted < k) {
      stack.pop();
      deleted += 1;
    }
    stack.push(x);
  });

  while (deleted < k) {
    stack.pop();
    deleted += 1;
  }

  return stack.join("");
}
