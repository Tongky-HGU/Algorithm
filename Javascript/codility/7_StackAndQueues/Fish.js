function solution(A, B) {
    //스택에 넣어 두었다가 다먹엇을 시에는 + 1
    let stack = [0]
    let i = 1
    while( i < A.length) {
        if(B[i]== 0 && B[stack[stack.length-1]] == 1){
            if(A[i]>A[stack[stack.length-1]]){
                stack.pop()
            }else{
                i++
            }
        }else{
            stack.push(i)
            i++
        }
    }
    return stack.length
}