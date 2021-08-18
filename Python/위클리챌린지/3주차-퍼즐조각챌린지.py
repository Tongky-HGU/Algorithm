def rotatePuzzle(puzzle):
    puzzle1 = []
    puzzle2 = []
    puzzle3 = []

    for r,c in puzzle:
        puzzle1.append([c,-r])
        puzzle2.append([-c,r])
        puzzle3.append([-r,-c])
    
    puzzle.sort()
    puzzle1.sort()
    puzzle2.sort()
    puzzle3.sort()
    return [ puzzle,puzzle1,puzzle2,puzzle3]    


def getPuzzle(table):
    N = len(table)
    vis = [[0 for _ in range(N)] for _ in range(N)]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    puzzles = {}
    queue = []
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1 and vis[i][j] == 0:
                queue.append([i,j])
                vis[i][j] = 1
                puzzle = []
                while(queue):
                    r,c = queue.pop();
                    puzzle.append([r-i,c-j])
                    for k in range(4):
                        cr = r+dr[k]
                        cc = c+dc[k]
                        if cr < 0 or cr >= N or cc < 0 or cc >=N : continue
                        if vis[cr][cc] == 1: continue
                        if table[cr][cc] == 0: continue
                        vis[cr][cc] = 1
                        queue.append([cr,cc])
                puzzles[len(puzzles)] = rotatePuzzle(puzzle)
    return puzzles

def fixHole(table,puzzles):
    fixedHole = 0
    N = len(table)
    used = [0 for _ in range(len(puzzles))]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    queue = []
    for i in range(N):
        for j in range(N):
            if table[i][j] == 0:
                vis = [[0 for _ in range(N)] for _ in range(N)]
                queue.append([i,j])
                vis[i][j] = 1
                hole = []
                while(queue):
                    r,c = queue.pop();
                    hole.append([r-i,c-j])
                    for k in range(4):
                        cr = r+dr[k]
                        cc = c+dc[k]
                        if cr < 0 or cr >= N or cc < 0 or cc >=N : continue
                        if vis[cr][cc] == 1: continue
                        if table[cr][cc] == 1: continue
                        vis[cr][cc] = 1
                        queue.append([cr,cc])
                fixed = False
                hole.sort()
                print("hole ")
                print(hole)
                for k in range(len(puzzles)):
                    if fixed: break
                    if used[k] == 1: continue
                    if len(hole) != len(puzzles[k][0]): continue
                    # print("puzzle")
                    for puzzle in puzzles[k]:
                        # print(puzzle)
                        if hole == puzzle:
                            fixedHole += len(hole)
                            fixed = True
                            used[k] = 1
                            print(hole, puzzle)
                            for x,y in hole:
                                table[i+x][j+y] = 1
                            break
    return fixedHole


def solution(game_board, table):
    puzzles = getPuzzle(table)
    return fixHole(game_board,puzzles);



# print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
# print(solution([[0,0,0],[1,1,0],[1,1,1]],[[1,1,1],[1,0,0],[0,0,0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]],[[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]))
#54
# print(solution([[1,0,0],[1,0,0],[1,0,0]], [[0,1,1],[0,1,1],[0,1,1]])) #6
# print(solution([[0,0,0],[0,0,0],[0,0,0]], [[1,1,1],[1,1,1],[1,1,1]])) #9
