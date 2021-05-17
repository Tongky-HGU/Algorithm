// 튜플
function solution(s) {
    let A = s.slice(2,s.length-2).split('},{')
    let words = []
    A.forEach((parsed)=>{
        words.push(parsed.split(','))
    })
    
    words.sort(function(a,b){
        return a.length - b.length
    })
    
    // console.log(words)
    
    let ans = new Set()
    
    for(let i = 0; i < words.length; i++){
        for(let j = 0; i < words[i].length; j++){
            if(!ans.has(Number(words[i][j]))){
                // console.log(words[i][j])
                ans.add(Number(words[i][j]))
                break
            }
        }
    }
    return [...ans];
}

//! best ans
const tupleFrom = (str) =>
  str.slice(2, -2).split('},{')
    .map((it) => toNumbers(it))
    .sort(accendingByLength)
    .reduce((acc, cur) =>
      [...acc, ...cur.filter((it) => !acc.includes(it))], []);

const toNumbers = (str) => str.split(',').map(it => Number(it));

const accendingByLength = (arr1, arr2) => arr1.length - arr2.length;

const solution = (s) => tupleFrom(s);