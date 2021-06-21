function solution(S, P, Q) {
    //index 찾는 방법 최소부터 찾는다
    let ans = []
    const word = ['A', 'C', 'G', 'T']
    for (let i = 0; i < P.length; i++) {
        let temp = S.slice(P[i], Q[i] + 1)
        let min = word.findIndex(a => temp.indexOf(a) != -1)
        ans.push(min+1)
    }
    return ans
}