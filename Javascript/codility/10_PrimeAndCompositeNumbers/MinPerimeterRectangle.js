function solution(N) {
    // i*i 로 커플 찾으면서 최소값 검사
    let ans = Infinity
    let i = 0
    while (i * i < N) {
        if (N % i == 0) ans = Math.min(ans, 2 * (i + N / i))
        i++
    }

    if (i*i == N) ans = Math.min(ans, 4*i)
    
    return ans
}