function rotatePuzzle(puzzle) {
    let puzzle90 = [];
    let puzzle180 = [];
    let puzzle270 = [];

    for (let [r, c] of puzzle) {
        puzzle90.push([c, -r]);
        puzzle180.push([-c, r]);
        puzzle270.push([-r, -c]);
    }
    puzzle.sort((a, b) => (a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0]));
    puzzle90.sort((a, b) => (a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0]));
    puzzle180.sort((a, b) => (a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0]));
    puzzle270.sort((a, b) => (a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0]));

    return [puzzle, puzzle90, puzzle180, puzzle270];
}

function getPuzzles(table) {
    const N = table.length;
    const dr = [0, 1, 0, -1];
    const dc = [1, 0, -1, 0];
    let puzzles = new Map();
    let stack = [];

    for (let i of Array(N).keys()) {
        for (let j of Array(N).keys()) {
            if (table[i][j] === 1) {
                stack.push([i, j]);
                table[i][j] = 0;
                let puzzle = [];
                while (stack.length) {
                    let [r, c] = stack.pop();
                    puzzle.push([r - i, c - j]);
                    for (let k of Array(4).keys()) {
                        let cr = r + dr[k];
                        let cc = c + dc[k];
                        if (cr < 0 || cr >= N || cc < 0 || cc >= N) continue;
                        if (table[cr][cc] === 0) continue;
                        table[cr][cc] = 0;
                        stack.push([cr, cc]);
                    }
                }
                puzzles[Object.keys(puzzles).length] = rotatePuzzle(puzzle);
            }
        }
    }
    return puzzles;
}

function fixHoles(table, puzzles) {
    const N = table.length;
    const dr = [0, 1, 0, -1];
    const dc = [1, 0, -1, 0];
    let fixedHole = 0;
    let used = new Array(Object.keys(puzzles).length).fill(0);
    let stack = [];
    for (let i of Array(N).keys()) {
        for (let j of Array(N).keys()) {
            if (table[i][j] === 0) {
                let vis = Array.from(Array(N), () => Array(N).fill(0));
                stack.push([i, j]);
                vis[i][j] = 1;
                let hole = [];
                while (stack.length) {
                    let [r, c] = stack.pop();
                    hole.push([r - i, c - j]);
                    for (let k of Array(4).keys()) {
                        let cr = r + dr[k];
                        let cc = c + dc[k];
                        if (cr < 0 || cr >= N || cc < 0 || cc >= N) continue;
                        if (vis[cr][cc] === 1) continue;
                        if (table[cr][cc] === 1) continue;
                        vis[cr][cc] = 1;
                        stack.push([cr, cc]);
                    }
                }
                let fixed = false;
                hole.sort((a, b) => (a[0] - b[0] === 0 ? a[1] - b[1] : a[0] - b[0]));
                for (let k of Array(Object.keys(puzzles).length).keys()) {
                    if (fixed) break;
                    if (used[k] === 1) continue;
                    if (hole.length !== puzzles[k][0].length) continue;
                    for (let puzzle of puzzles[k]) {
                        if (JSON.stringify(hole) === JSON.stringify(puzzle)) {
                            fixedHole += hole.length;
                            fixed = true;
                            used[k] = 1;
                            for (let [x, y] of hole) {
                                table[i + x][j + y] = 1;
                            }
                            break;
                        }
                    }
                }
            }
        }
    }
    return fixedHole;
}

function solution(game_board, table) {
    const puzzles = getPuzzles(table);
    return fixHoles(game_board, puzzles);
}

console.log(
    solution(
        [
            [1, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0, 1],
            [1, 1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0, 0],
        ],
        [
            [1, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0, 0],
            [1, 1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 0],
        ]
    )
);
