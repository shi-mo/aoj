#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main()
{
    int n, q, query;
    vector<queue<long>> que;

    cin >> n;
    cin >> q;
    que.resize(n);
    while (cin >> query) {
        int t;
        cin >> t;
        switch (query) {
        case 0: // enqueue(t, x)
            int x;
            cin >> x;
            que[t].push(x);
            break;
        case 1: // front(t)
            if (!que[t].empty()) {
                cout << que[t].front() << endl;
            }
            break;
        case 2: // dequeue(t)
            if (!que[t].empty()) {
                que[t].pop();
            }
        }
    }
    que.clear();
}
