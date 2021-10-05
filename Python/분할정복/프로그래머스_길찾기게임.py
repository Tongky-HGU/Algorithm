import sys
sys.setrecursionlimit(10**6)


def solution(nodeInfo):
    preorder = []
    postorder = []

    nodes = sorted(list(zip(range(1, len(nodeInfo)+1), nodeInfo)),
                   key=lambda x: (-x[1][1], x[1][0]))

    def check(node):
        cur = node[0]
        preorder.append(cur[0])
        if len(node) > 1:
            left = list(
                filter(lambda x: x[1][0] < cur[1][0] and x[1][1] < cur[1][1], node))
            right = list(
                filter(lambda x: x[1][0] > cur[1][0] and x[1][1] < cur[1][1], node))
            if len(left):
                check(left)
            if len(right):
                check(right)
        postorder.append(cur[0])

    check(nodes)

    return [preorder, postorder]
