function solution(A, B, K) {
    // B//K
    // a가 0일때는 +1, 아닐때는 (a-1)/k 빼준다
    if (A==0){
        return Math.floor(B/K) + 1
    }else{
        return Math.floor(B/K) - Math.floor((A-1)/K)
    }
}