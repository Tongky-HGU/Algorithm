function solution(A) {
    // 절대값 씌워서 set에서 넣으면 되자 않나
    let set = new Set()
    for(a of A){
        set.add(Math.abs(a))
    }
    return set.size
}