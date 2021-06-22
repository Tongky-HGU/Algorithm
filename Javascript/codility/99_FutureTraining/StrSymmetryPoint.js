function solution(S) {
    // 길이가 1일때 예외처리
    if (S.length == 1) return 0

    // 길이가 짝수여도 제외처리
    if (S.length % 2 == 0) return -1

    // 반대가 같으면 return true
    let L = S.slice(0, Math.ceil(S.length / 2) - 1)
    let R = ([...S.slice(Math.ceil(S.length / 2))].reverse().join(''))
    // console.log(L, R)
    if (L == R) return Math.ceil(S.length / 2) - 1
    return -1
}