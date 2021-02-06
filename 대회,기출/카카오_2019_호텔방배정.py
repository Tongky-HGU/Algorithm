import sys
sys.setrecursionlimit(10**7)
def solution(k, room_number):
    def find(a):
        if a not in room:
            room[a] = a
            return a
        room[a] = find(room[a]+1)
        return room[a]
    room = {}
    ans = [0 for _ in range(len(room_number))]
    for i in range(len(room_number)):
        ans[i] = find(room_number[i])
    return ans