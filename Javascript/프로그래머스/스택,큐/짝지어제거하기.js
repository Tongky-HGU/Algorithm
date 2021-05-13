//짝지어 제거하기
function solution(s)
{
    if(s.length % 2 != 0) return 0

    const stack = []
    stack.push(s[0])
    for(let i = 1; i < s.length; i++){
        if(s[i] == stack[stack.length-1]){
            stack.pop()
        }else{
            stack.push(s[i])
        }
    }
    if(stack.length == 0){
        return 1
    }
    return 0;
}