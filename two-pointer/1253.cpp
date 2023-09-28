#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void point(const vector<int>& lst) {
	int cnt = 0;
	for (int target : lst) {
		vector<int> tmp(lst);
		auto x = find(tmp.begin(), tmp.end(), target);
		if (x != tmp.end())
			tmp.erase(x);

		int left = 0, right = tmp.size() - 1;
		while (left < right) {
			int add = tmp[left] + tmp[right];
			if (add == target) {
				cnt++;
				break;
			}
			else if (add < target)
				left++;
			else
				right--;
		}
	}
	cout << cnt << endl;	
}
int main(void) {
	int N;
	cin >> N;
	vector<int> lst(N);
	for (int i = 0; i < N; i++) {
		cin >> lst[i];
	}
	sort(lst.begin(), lst.end());
	point(lst);
	return 0; 
}
