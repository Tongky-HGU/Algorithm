function solution(A) {
    //object 에 추가하 하고, 절반 이상인 요소가 있는 지 확인 
    let set = {}
    let half = A.length / 2
    if (A.length == 1) return 0
    for (let i = 0; i < A.length; i++) {
        if(set[A[i]]){
            set[A[i]].push(i)
            if ( set[A[i]].length > half) return set[A[i]][0]
        }else{
            set[A[i]] = [i]
        }
    }
    return -1
}