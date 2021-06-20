function solution(A) {
    let ans = 0
    // 배열 만들어 가지고 있는 애 표시
    let vis = new Array(A.length+1).fill(0)
    A.forEach((a)=>{
        vis[a] = 1
    })

    // 없는 숫자 리턴
    for(let i = 1; i <= vis.length; i++){
        if(!vis[i]){
            return i
        }
    }
}