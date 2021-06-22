function solution(N, M) {
    // 유클리드 호제법. 최대 공약수를 소인수 분해보다 빨리 찾음
    function GCD(N, M) {
        if (M === 0) return N
        return GCD(M,N%M)
    }

    let gcd = GCD(N,M)

    return parseInt(N/gcd)
}