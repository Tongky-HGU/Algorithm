/*
10808
알파벳 소문자로만 이루어진 단어 S가 주어진다. 
각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
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
총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
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
두 개의 문자열에 대해,2번째 문자열이 1번째 문자열에 
strfry 함수를 적용하여 얻어질 수 있는지 판단하라.
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
한 방에 배정할 수 있는 최대 인원 수 K가 주어졌을 때, 조건에 맞게
모든 학생을 배정하기 위해 필요한 방의 최소 개수를 구하는 프로그램을 작성하시오.
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
다솜이는 은진이의 옆집에 새로 이사왔다.
다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 
한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 
다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. 
(6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)
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
두 개의 영어 단어가 주어졌을 때,
두 단어가 서로 애너그램 관계에 있도록 만들기 위해서 
제거해야 하는 최소 개수의 문자 수를 구하는 프로그램을 작성하시오.
문자를 제거할 때에는 아무 위치에 있는 문자든지 제거할 수 있다.
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