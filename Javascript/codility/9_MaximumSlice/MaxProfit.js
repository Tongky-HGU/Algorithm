function solution(A) {
    // 저점을 기억해두고,
    // 더 낮다면 갱신, 높다면 ans 갱신
    let min = 200000
    let ans = 0
    for (a of A) {
        if(a < min){
            min = a
        }else{
            ans = Math.max(ans,a-min)
        }
    }
    return ans
}