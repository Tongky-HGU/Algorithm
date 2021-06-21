function solution(S) {
    // 스택에 넣고 나머지가 있거나 안맞은면 FALSE   
    const L = new Set(['(', '{', '['])
    const R = new Set([']', '}', ')'])
    const match = { '(': ')', '{': '}', '[': ']' }
    let stack = []
    for (char of S) {
        if (L.has(char)) {
            stack.push(char)
        } else if (R.has(char)) {
            lastest = stack.pop()
            if (match[lastest] != char) {
                return 0
            }
        }
    }

    if (stack.length) return 0
    return 1
}