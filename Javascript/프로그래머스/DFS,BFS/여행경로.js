function solution(tickets) {
    var ans = [];

    const dfs = (a,tickets,path) =>{
        var newPath = [...path,a]
        if(tickets.length == 0){
            ans.push(newPath)
            return
        }    
        tickets.map((ticket,idx) =>{
            if(ticket[0]===a){
                var temp = [...tickets]
                var [[cur,to]] = temp.splice(idx,1)
                dfs(to,temp,newPath)
            }
        })
    }
    
    dfs("ICN",tickets,[])
    
    return ans.sort()[0];
}