//9663 N-Queen
#include <bits/stdc++.h>
using namespace std;
int n;
int cnt = 0;
bool isused1[16];
bool isused2[32];
bool isused3[32];
void func(int k) {
	if (k==n) {
		cnt++;
		return;
	}
	for (int i = 0; i < n; i++) {
		if (!isused1[i] and !isused2[i+k] and !isused3[k-i+n-1]) {
			isused1[i] = 1;
			isused2[i+k] = 1;
			isused3[k-i+n-1] = 1;
			func(k + 1);
			isused1[i] = 0;
			isused2[i+k] = 0;
			isused3[k-i+n-1] = 0;
		}
	}
}
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	func(0);
	cout << cnt;
}
