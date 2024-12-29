#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main()
{
    int n, q, query;
    vector<stack<long>> st;

    cin >> n;
    cin >> q;
    st.resize(n);
    while (cin >> query) {
        int t;
        cin >> t;
        switch (query) {
        case 0: // push(t, x)
            int x;
            cin >> x;
            st[t].push(x);
            break;
        case 1: // top(t)
            if (!st[t].empty()) {
                cout << st[t].top() << endl;
            }
            break;
        case 2: // pop(t)
            if (!st[t].empty()) {
                st[t].pop();
            }
        }
    }
    st.clear();
}
