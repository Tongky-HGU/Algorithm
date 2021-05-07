// 타겟넘버
function solution(numbers, target) {
    var ans = 0;
    function dfs(a,cnt){
        // console.log(a,cnt)
        
        if (cnt === numbers.length -1){
            if (a === target ){
                ans +=1
            }
            return
        }
        for (var i=0; i < 1; i++){
            dfs(a+numbers[cnt+1],cnt+1)
            dfs(a-numbers[cnt+1],cnt+1)
        }
    }
    
    dfs(numbers[0],0)
    dfs(-numbers[0],0)
    // console.log(ans)
    
    return ans;
}