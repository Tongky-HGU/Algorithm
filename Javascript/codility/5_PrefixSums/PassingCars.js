function solution(A) {
    let ans = 0
    let R = 0
    for (a of A) {
        if (a) {
            R += 1
        }
    }
    for (a of A) {
        if (a) {
            R -= 1
        } else {
            ans += R
        }
        if (ans > 1000000000) return -1
    }

    return ans
}