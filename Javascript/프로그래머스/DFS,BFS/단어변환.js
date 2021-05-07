function solution(begin, target, words) {
    var ans = 0;
    var vis = new Array(words.length).fill(0)
    var queue = new Array()
    
    queue.push([begin,0])

    function check(a,b){
        var cnt = 0
        a = a.split("")
        b = b.split("")
        for (var i=0; i < a.length; i++){
            if(a[i]!==b[i]) cnt += 1
        }
        if (cnt === 1) return 1
        return 0
    }
    
    while(queue.length){
        var [cur,cnt] = queue.shift()
        if (cur === target) return cnt
        words.forEach((word,index)=>{
            if (!vis[index] && check(word,cur)){
                vis[index] = 1
                queue.push([word,cnt+1])            
            }
        })
    }
    
    return ans;
}  