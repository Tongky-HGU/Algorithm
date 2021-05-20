// 뉴스클러스터링
function solution(str1, str2) {
    let ans = 0;
    console.log(str1,str2)
    
    const isAlpha = (str) =>{
        return str.length === 1 && str.match(/[a-z]/i);
    }
    
    const splitWord = (str) =>{
        let ret = []
        for(let i=0;i<str.length-1;i++){
            if (!isAlpha(str[i]) || !isAlpha(str[i+1])) continue
            // if (ret.includes(str.slice(i,i+2).toUpperCase())) continue
            ret.push(str.slice(i,i+2).toUpperCase())
        }
        return ret
    }
    
    let A = splitWord(str1)
    let B = splitWord(str2)
    
    // console.log(A,B)
    
    let total = 0
    let union = 0
    
    B.forEach((str)=>{
        if(A.includes(str)){
            union += 1
            const idx = A.indexOf(str)
            A.splice(idx,1)
        }else{
            total += 1
        }
    })
    
    total += A.length + union
    
    // console.log(union,total)
    
    ans = parseInt(union/total*65536)
    if(isNaN(ans)) ans = 65536
    return ans
}