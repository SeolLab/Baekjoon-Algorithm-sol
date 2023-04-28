// 15650 N과 M(2) c++
#include <iostream>
using namespace std;
int n, m;
int arr[8];
bool isused[8];

void refunc(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++)
			cout << arr[i] << " ";
	cout << '\n';
	return;
	}
	for (int i = 1; i <= n; i++) {
		if (not isused[i] and k == 0) {
			arr[k] = i;
			isused[i] = 1;
			refunc(k + 1);
			isused[i] = 0;
		}
		if (not isused[i] and arr[k-1]<i and k > 0) {
			arr[k] = i;
			isused[i] = 1;
			refunc(k+1);
			isused[i] = 0;
		}
	}
}
int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> m;
	refunc(0);
}
