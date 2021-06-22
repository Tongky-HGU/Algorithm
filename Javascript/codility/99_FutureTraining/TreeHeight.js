function solution(T) {
    //dfs 로 파싱해가면서 None을 만났을 떄 최대 depth 구하기
    let ans = 0
    function dfs(input, cnt) {
        // console.log(input)
        if (!input['l'] && !input['r']) {
            ans = Math.max(ans, cnt)
        } else {
            if (input['l']) {
                dfs(input['l'], cnt + 1)
            }
            if (input['r']) {
                dfs(input['r'], cnt + 1)
            }
        }
    }

    dfs(T, 0)
    return ans
}