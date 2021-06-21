// for char of string 이 느려서 타임오버됨
function solution(S) {
  // 스택에 넣고 짝이 안맞거나 나머지 있으면 false
  let stack = [];
  for (let i = 0; i < S.length; i++) {
    if (S[i] == "(") {
      stack.push(S[i]);
    } else {
      if (stack.length) {
        stack.pop();
      } else {
        return 0;
      }
    }
  }
  if (stack.length) return 0;
  return 1;
}
