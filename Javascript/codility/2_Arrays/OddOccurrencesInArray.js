function solution(A) {
    // set에 추가해가며 중복 된 것은 제거
    let check = new Set()
    
    A.forEach((a)=>{
        if (check.has(a)){
            check.delete(a)
        }else{
            check.add(a)
        }
    })
    // 남은 하나 return
    ans = [...check][0]
    return ans
}