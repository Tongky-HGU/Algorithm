//N의 최소공배수
function solution(arr) {
    let ans = 0;
    let i = 1
    while(1){
        let flag = true
        arr.forEach((a)=>{
            if (i % a != 0) flag = false
        })
        
        if(flag){
            ans = i
            break
        }
        i++
    }
    return ans;
}