function solution(N) {
    // i*i 가 N 을 넘지 않으면서  N%i == 0 인지 확인
    let i = 0
    let ans = 0

    while (i * i < N) {
        if (N % i == 0) ans += 2
        i++
    }

    if (i * i == N) ans += 1

    return ans
}