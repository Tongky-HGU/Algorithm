/*
10808
���ĺ� �ҹ��ڷθ� �̷���� �ܾ� S�� �־�����. 
�� ���ĺ��� �ܾ �� ���� ���ԵǾ� �ִ��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	string s;
//	int a[26] = {};
//	cin >> s;
//	for (int i = 0; i < s.length(); i++) {
//		a[int(s[i]) - 97]++;
//	}
//	for (int i = 0; i < 26; i++) {
//		cout << a[i] << " ";
//	}
//}

/*
10807.
�� N���� ������ �־����� ��, ���� v�� �� ������ ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
*/
//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int n, arr[100], v, ans = 0;
//	cin >> n;
//	for (int i = 0; i < n; i++) {
//		cin >> arr[i];
//	}
//	cin >> v;
//	for (int i = 0; i < n; i++) {
//		if (arr[i] == v) ans++;
//	}
//	cout << ans;
//}

/*
11328.
�� ���� ���ڿ��� ����,2��° ���ڿ��� 1��° ���ڿ��� 
strfry �Լ��� �����Ͽ� ����� �� �ִ��� �Ǵ��϶�.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int n =0;
//	int a[26] = {};
//	string as, bs;
//	cin >> n;
//	for (int i = 0; i < n; i++) {
//		cin >> as >> bs;
//		fill(a, a + 26, 0);
//		bool ans = true;
//		for (int j = 0; j < as.length(); j++) {
//			a[int(as[j]) - 97]++;
//			a[int(bs[j]) - 97]--;
//		}
//		for (int j = 0; j < 26 ; j++) {
//			if (a[j] != 0) {
//				cout << "Impossible\n";
//				ans = false;
//				break;
//			}
//		}
//		if (ans) cout << "Possible\n";
//	}
//}

/*
13300.
�� �濡 ������ �� �ִ� �ִ� �ο� �� K�� �־����� ��, ���ǿ� �°�
��� �л��� �����ϱ� ���� �ʿ��� ���� �ּ� ������ ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	int member[12] = {}, year, gender, n, k, ans=0;
//	cin >> n >> k;
//	for (int i = 0; i < n; i++) {
//		cin >> gender >> year;
//		member[6 * gender + year - 1]++;
//	}
//	for (int i = 0; i <12; i++)	{
//		if (member[i] % k !=0) ans++;
//		ans += member[i]/k;
//	}
//	cout << ans;
//}

/*
1475.
�ټ��̴� �������� ������ ���� �̻�Դ�.
�ټ��̴� �ڱ� �� ��ȣ�� ���� �ö�ƽ ���ڷ� ���� ���̷��� �Ѵ�.

�ټ����� ���������� �ö�ƽ ���ڸ� �� ��Ʈ�� �Ǵ�. 
�� ��Ʈ���� 0������ 9������ ���ڰ� �ϳ��� ����ִ�. 
�ټ����� �� ��ȣ�� �־����� ��, �ʿ��� ��Ʈ�� ������ �ּڰ��� ����Ͻÿ�. 
(6�� 9�� ����� �̿��� �� �ְ�, 9�� 6�� ����� �̿��� �� �ִ�.)
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	string num;
//	int ans[10] = {}, max = 0;
//	cin >> num;
//	for (int i = 0; i < num.length(); i++)	{
//		ans[int(num[i]) - 48] ++ ;
//	}
//	ans[6] = ((ans[6] + ans[9]) * 10 / 2 + 5) / 10;
//	for (int i = 0; i < 9; i++)	{
//		if (ans[i] > max) max = ans[i];
//	}
//	cout << max;
//}

/*
1919.
�� ���� ���� �ܾ �־����� ��,
�� �ܾ ���� �ֳʱ׷� ���迡 �ֵ��� ����� ���ؼ� 
�����ؾ� �ϴ� �ּ� ������ ���� ���� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
���ڸ� ������ ������ �ƹ� ��ġ�� �ִ� ���ڵ��� ������ �� �ִ�.
*/

//#include <bits/stdc++.h>
//using namespace std;
//int main(void) {
//	cin.tie(0);
//	ios::sync_with_stdio(0);
//	string s;
//	int arr[26] = {}, ans = 0;
//	cin >> s;
//	for (int i = 0; i < s.length(); i++) {
//		arr[int(s[i] - 97)] ++;
//	}
//	cin >> s;
//	for (int i = 0; i < s.length(); i++) {
//		arr[int(s[i] - 97)] --;
//	}
//	for (int i = 0; i < 26; i++) {
//		if (arr[i] > 0) ans += arr[i];
//		else if (arr[i] < 0) ans -= arr[i];
//	}
//	cout << ans;
//}