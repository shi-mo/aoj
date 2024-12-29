#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, q, query;
    vector<vector<long>> v;

    cin >> n;
    cin >> q;
    v.resize(n);
    while (cin >> query) {
        int t;
        cin >> t;
        switch (query) {
        case 0: // pushBack(t, x)
            int x;
            cin >> x;
            v[t].push_back(x);
            break;
        case 1: // dump(t)
            for (auto itr = v[t].begin(); itr != v[t].end(); itr++) {
                if (v[t].begin() != itr) cout << " ";
                cout << *itr;
            }
            cout << endl;
            break;
        case 2: // clear(t)
            v[t].clear();
        }
    }
    v.clear();
}
