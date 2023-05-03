#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int a, b, m;
vector <int> arr = {1,2,3};


int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		swap(arr[a - 1], arr[b - 1]);
	}
	for (int i = 0; i < 3; i++) {
		if (arr[i] == 1) cout << i + 1;
	}
}
