//#include <bits/stdc++.h>
//using namespace std;
//
//const int MX = 1000005;
//int dat[MX], pre[MX], nxt[MX];
//int unused = 1;
//
//void insert(int addr, int num) {
//	dat[unused] = num;
//	pre[unused] = addr;
//	nxt[unused] = nxt[addr];
//	nxt[addr] = unused;
//	if(nxt[addr]!=-1) pre[nxt[unused]] = unused;
//	unused++;
//}
//
//void erase(int addr) {
//	if (nxt[addr] != -1)pre[nxt[addr]] = pre[addr];
//	nxt[pre[addr]] = nxt[addr];
//}
//
//void traverse() {
//	int cur = nxt[0];
//	while (cur != -1) {
//		cout << dat[cur] << ' ';
//		cur = nxt[cur];
//	}
//	cout << "\n\n";
//}
//
//void insert_test() {
//	cout << "****** insert_test *****\n";
//	insert(0, 10); // 10(address=1)
//	traverse();
//	insert(0, 30); // 30(address=2) 10
//	traverse();
//	insert(2, 40); // 30 40(address=3) 10
//	traverse();
//	insert(1, 20); // 30 40 10 20(address=4)
//	traverse();
//	insert(4, 70); // 30 40 10 20 70(address=5)
//	traverse();
//}
//
//void erase_test() {
//	cout << "****** erase_test *****\n";
//	erase(1); // 30 40 20 70
//	traverse();
//	erase(2); // 40 20 70
//	traverse();
//	erase(4); // 40 70
//	traverse();
//	erase(5); // 40
//	traverse();
//}
//
//int main(void) {
//	fill(pre, pre + MX, -1);
//	fill(nxt, nxt + MX, -1);
//	insert_test();
//	erase_test();
//}
//
///////////////////////////////////////////////////////////////////////
//
//#include <bits/stdc++.h>
//using namespace std;
//
//int main(void) {
//	list<int> L = { 1,2 }; // 1 2
//	list<int>::iterator t = L.begin(); // t는 1을 가리키는 중
//	L.push_front(10); // 10 1 2
//	cout << *t << '\n'; // t가 가리키는 값 = 1을 출력
//	L.push_back(5); // 10 1 2 5
//	L.insert(t, 6); // t가 가리키는 곳 앞에 6을 삽입, 10 6 1 2 5
//	t++; // t를 1칸 앞으로 전진, 현재 t가 가리키는 값은 2
//	t = L.erase(t); // t가 가리키는 값을 제거, 그 다음 원소인 5의 위치를 반환
//					// 10 6 1 5, t가 가리키는 값은 5
//	cout << *t << '\n'; // 5
//	for (auto i : L) cout << i << ' ';
//	cout << '\n';
//	for (list<int>::iterator it = L.begin(); it != L.end(); it++)
//		cout << *it << ' ';
//}