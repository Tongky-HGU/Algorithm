// replace를 써서 '' 로 바꾸고 legnth를 했으면 더 효율적이었겠다.

function solution(S) {
    // split 해서 조건들 체크
    // 길이가 max값인 것 저장
    let ans = -1
    let candis = S.split(' ')
    for (candi of candis) {
        if (candi.match(/[^A-Za-z0-9]/) == null) {
            let letter = candi.match(/[A-Za-z]/g)
            let digit = candi.match(/[0-9]/g)

            if (letter != null) {
                if (letter.length % 2 == 1) continue
            } 

            if (digit != null) {
                if (digit.length % 2 == 0) continue
            } else {
                // 0 은 짝수다..
                continue
            }

            // console.log(candi)
            ans = Math.max(ans, candi.length)
        }
    }
    return ans
}