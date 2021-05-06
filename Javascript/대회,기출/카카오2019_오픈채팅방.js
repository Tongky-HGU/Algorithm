function solution(record) {
    var ans = []
    var A = []
    var id = {}
    
    record.forEach((string) => {
        string = string.split(" ")
        if (string[0] === "Enter") {
            A.push([0,string[1]])
            id[string[1]] = string[2]
        }else if (string[0] === "Leave"){
            A.push([1,string[1]])
        }else{
            id[string[1]] = string[2]
        }
    })
    
    A.forEach((i) =>{
        // console.log(i)
        if (i[0] == 0){
            ans.push(id[i[1]]+"님이 들어왔습니다.")
        }else{
            ans.push(id[i[1]]+"님이 나갔습니다.")
        }
    })
    // console.log(ans)
    return ans;
}