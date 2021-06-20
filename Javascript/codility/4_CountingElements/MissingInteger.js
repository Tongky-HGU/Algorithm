function solution(A) {
    let ans = 1
    let X = new Set(A)
    while (1) {
        if (!X.has(ans)) {
            return ans
        }
        ans++
    }
}