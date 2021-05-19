// N으로 표현
function solution(N, number) {
    let ans = 0;
    
    const s = [new Set()]
    for (let i=1;i<=8;i++){
        s.push(new Set([new Array(i).fill(N).join('') * 1]))
        for (let j=1; j<=i;j++){
            for (const a of [...s[j]]){
                for (const b of [...s[i-j]]){
                    s[i].add(a+b)
                    s[i].add(a-b)
                    s[i].add(a*b)
                    s[i].add(parseInt(a/b))
                }
            }
        }
        // console.log([...s[i]])
        if (s[i].has(number)){
            return i
        }
    }
    
    // console.log(s)
    
    return -1;
}