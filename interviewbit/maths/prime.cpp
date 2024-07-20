#include <iostream>
#include <vector>
using namespace std;

void printAllElements(const vector<int>& vec) {
    cout << "(";
    for (int i : vec) {
        cout << i << " ";
    }
    cout << ")" << endl;
}

int main() {
    int A = 1;
    vector<vector<int> > ans;
    for (int b = 1; b * b <= A; b++) {
        for (int a = 0; a <= b && a * a <= A; a++) {
            if (a * a + b * b == A) {
                vector<int> newEntry;
                newEntry.push_back(a);
                newEntry.push_back(b);
                ans.push_back(newEntry);
            }
        }
    }
    for (auto v : ans) {
        printAllElements(v);
    }
}