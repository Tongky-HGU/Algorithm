function solution(priorities, location) {
    let ans = 0;
    let cnt = 0
    
    while(priorities.length){
        let cur = priorities.shift()
        if (priorities.filter((e)=> e > cur).length){
            priorities.push(cur)
        }else{
            cnt++
            if(location == 0){
                return cnt
            }
        }
        location--
        if(location == -1){
            location = priorities.length-1
        }
    }
    
    return ans;
}