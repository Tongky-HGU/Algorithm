#표편집
class node:
    def __init__(self,key,prev=None,nex=None):
        self.key = key
        self.prev = prev
        self.next = nex

def solution(n, k, cmds):
    data = [_ for _ in range(n)]
    for i in range(n):
        data[i] = node(i,i-1,i+1)

    data[0].prev = None
    data[n-1].next = None

    stack = []

    cur = k 

    def up(cnt):
        nonlocal cur
        for _ in range(cnt):
            cur = data[cur].prev    

    def down(cnt):
        nonlocal cur
        for _ in range(cnt):
            cur = data[cur].next

    def delete():
        nonlocal cur
        stack.append(cur)
        if data[cur].prev != None:
            data[data[cur].prev].next = data[cur].next
        if data[cur].next != None:
            data[data[cur].next].prev = data[cur].prev
        if data[cur].next == None:
            cur = data[cur].prev
        else:
            cur = data[cur].next

    def restore():
        res = stack.pop()
        if data[res].prev != None:
            data[data[res].prev].next = res
        if data[res].next != None:
            data[data[res].next].prev = res

    for cmd in cmds:
        if cmd[0] == 'U':
            up(int(cmd[2:]))
        elif cmd[0] == "D":
            down(int(cmd[2:]))
        elif cmd[0] == "C":
            delete()
        elif cmd[0] == "Z":
            restore()
        print(cmd,cur,stack)

    ans = ['O' for _ in range(n)]
    for i in stack:
        ans[i]='X'
    return ''.join(ans)

print( solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))