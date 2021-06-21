function solution(A) {
    // set에 넣기만 하면 끝
    set = new Set
    for (a of A){
        set.add(a)
    }
    return set.size
}