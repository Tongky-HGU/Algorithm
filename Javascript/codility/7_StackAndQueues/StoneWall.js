function solution(H) {
    const N = H.length;
    let stack = [];
    let ans = 0;
    for(let i=0; i<N; i++){
        while(stack.length && H[i] < stack[stack.length-1]){
            stack.pop();
        }
        if(!stack.length || H[i] > stack[stack.length-1]){
            stack.push(H[i]);
            ans++;
        }
    }
    
    return ans;
}