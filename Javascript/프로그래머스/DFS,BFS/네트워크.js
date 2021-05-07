function solution(n, computers) {
    var ans = 0;
    var vis = new Array(n).fill(0)
    
    function dfs(a){
        if (vis[a]) return

        // console.log(a)
        
        vis[a] = 1
        computers[a].forEach((b,index) => {
            if (b && !vis[index]){
                dfs(index)
            } 
        })
    }
    
    for(var i=0; i<n; i++){
        if (!vis[i]){
            dfs(i)
            ans+=1
        }
    }
    
    // console.log(ans)
    return ans;
}