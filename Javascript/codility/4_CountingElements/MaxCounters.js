// 일일히 더해주지말고 마지막에만 더해주는게 포인트...
function solution(N, A) {
    //dp 만들고 해당 인덱스 +1
    //max 기억하고 있다가 적용
    let dp = new Array(N + 1).fill(0)
    let max = 0
    let maxCounter = 0
    for (a of A) {
        if (a <= N) {
            dp[a] = Math.max(maxCounter+1,dp[a]+1)
            max = Math.max(max,dp[a])
        } else {
            maxCounter = max
        }
    }
    dp.filter((a,idx)=>{dp[idx]= Math.max(maxCounter,dp[idx])})
    return dp.slice(1)
}