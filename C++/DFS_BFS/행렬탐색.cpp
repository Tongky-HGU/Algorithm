
#include <algorithm>
#include <iostream>
#include <queue>
#include <sstream>

using namespace std;

typedef pair<int, int> xy;
queue<xy> que;
int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};

void solution(int N, int **matrix) {
    // TODO: 이곳에 코드를 작성하세요.
    vector<int> ans;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (matrix[i][j] == 1) {
                int cnt = 0;
                que.push(make_pair(i, j));
                while (!que.empty()) {
                    int r = que.front().first;
                    int c = que.front().second;
                    que.pop();
                    cnt += 1;
                    matrix[r][c] = 2;
                    for (int k = 0; k < 4; k++) {
                        int cr = r + dr[k];
                        int cc = c + dc[k];
                        if (cr < 0 || cr >= N || cc < 0 || cc >= N) continue;
                        if (matrix[cr][cc] == 0 || matrix[cr][cc] == 2) continue;
                        matrix[cr][cc] = 2;
                        que.push(make_pair(cr, cc));
                    }
                }
                ans.push_back(cnt);
            }
        }
    }

    sort(ans.begin(), ans.end());
    cout << ans.size() << "\n";
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }
}

struct input_data {
    int sizeOfMatrix;
    int **matrix;
};

void process_stdin(struct input_data &inputData) {
    string line;
    istringstream iss;

    getline(cin, line);
    iss.str(line);
    iss >> inputData.sizeOfMatrix;

    inputData.matrix = new int *[inputData.sizeOfMatrix];
    for (int i = 0; i < inputData.sizeOfMatrix; i++) {
        getline(cin, line);
        iss.clear();
        iss.str(line);
        inputData.matrix[i] = new int[inputData.sizeOfMatrix];
        for (int j = 0; j < inputData.sizeOfMatrix; j++) {
            iss >> inputData.matrix[i][j];
        }
    }
}

int main() {
    struct input_data inputData;
    process_stdin(inputData);

    solution(inputData.sizeOfMatrix, inputData.matrix);
    return 0;
}