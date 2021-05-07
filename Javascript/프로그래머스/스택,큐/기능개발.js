// 기능 개발
function solution(progresses, speeds) {
    const N = progresses.length
    let ans = [1]
    let work = [Math.ceil((100 - progresses[0]) / speeds[0])]
    for(let i=1;i<N;i++){
        let a = Math.ceil((100 - progresses[i]) / speeds[i])
        if (a > work[work.length-1]){
            work.push(a)
            ans.push(1)
        }else{
            ans[work.length-1] += 1
        }
        // console.log(work , ans)
    }
    return ans;
}