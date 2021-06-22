// function solution(A) {
//     // for 문돌면서 자신보다 큰 인덱스가 작은 값을 가지는 경우 세기
//     let ans = 0
//     for (let i = 0; i < A.length - 1; i++) {
//         for (let j = i + 1; j < A.length; j++) {
//             if (A[i] > A[j]) ans += 1
//         }
//         if (ans > 1000000000) return -1
//     }
//     return ans
// }

function solution(A) {
    // merge sort
    ans = 0
    if (A.length <= 1) return ans

    function merge(a) {
        // console.log(a)
        if (a.length == 1) return a
        let L = merge(a.slice(0, Math.floor(a.length / 2)))
        let R = merge(a.slice(Math.floor(a.length / 2)))
        let ret = []
        while (L.length || R.length) {
            if (!L.length) {
                ret.push(R.shift())
                continue
            }
            if (!R.length) {
                ret.push(L.shift())
                continue
            }
            if (L[0] > R[0]) {
                ans += L.length
                ret.push(R.shift())
            } else {
                ret.push(L.shift())
            }
        }
        // console.log(ans)
        return ret
    }

    // console.log(merge(A))
    merge(A)
    if (ans > 1000000000) return -1

    return ans
}