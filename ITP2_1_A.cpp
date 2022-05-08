#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int q, query;
    vector<long> v;

    cin >> q;
    while (cin >> query) {
        switch (query) {
        case 0:
            int x;
            cin >> x;
            v.push_back(x);
            break;
        case 1:
            int p;
            cin >> p;
            cout << v[p] << endl;
            break;
        case 2:
            v.pop_back();
        }
    }
}
