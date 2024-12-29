#include <iostream>
#include <list>
#include <vector>
using namespace std;

int main()
{
    int n, q, query;
    vector<list<long>> lst;

    cin >> n;
    cin >> q;
    lst.resize(n);
    while (cin >> query) {
        int t;
        cin >> t;
        switch (query) {
        case 0: // insert(t, x)
            int x;
            cin >> x;
            lst[t].push_back(x);
            break;
        case 1: // dump(t)
            for (auto itr = lst[t].begin(); itr != lst[t].end(); itr++) {
                if (lst[t].begin() != itr) cout << " ";
                cout << *itr;
            }
            cout << endl;
            break;
        case 2: // splice(t, u)
            int u;
            cin >> u;
            lst[u].splice(lst[u].end(), lst[t]);
            lst[t].clear();
        }
    }
    lst.clear();
}
