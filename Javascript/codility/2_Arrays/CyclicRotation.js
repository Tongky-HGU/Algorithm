function solution(A, K) {
    // 나머지 만큼 idx 이동
    const idx = A.length - K%A.length
    let ans = [...A.slice(idx), ...A.slice(0,idx)]
    return ans
}