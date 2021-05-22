//입국심사
function solution(n, times) {
    let cl = 0
    let cr = Math.max(...times) * n
    let ans = cr;
    
    while(cl<=cr){
        let mid = Math.floor((cl+cr)/2)
        let cnt = 0
        times.forEach((a)=>{
            cnt += Math.floor(mid/a) 
            if(cnt >= n){
                ans = Math.min(ans,mid)
            }
        })
        
        if(cnt >= n){
           cr = mid -1
        }else{
           cl = mid +1
        }
    }
    // console.log(ans)
    return ans;
}