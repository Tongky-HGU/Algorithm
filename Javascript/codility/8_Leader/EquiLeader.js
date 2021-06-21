function solution(A) {
    // 객체 만들어서 추가하다가 leader가 나오면, 그 리더가 나머지에도 반이상 나오는지 확인
    let count = {}
    let ans = 0
    let max = 0
    for (let i = 0; i < A.length; i++) {
        if (count[A[i]]) {
            count[A[i]] += 1
            if (count[A[i]] > A.length / 2) max = A[i]
        } else {
            count[A[i]] = 1
        }
    }

    let cnt = 0
    let L = 0
    let R = A.length
    for (let i = 0; i < A.length; i++) {
        L += 1
        R -= 1
        if (A[i] == max) cnt += 1
        if (cnt > L / 2) {
            if (count[max] - cnt > R / 2) {
                ans += 1
            }
        }
    }

    return ans
}