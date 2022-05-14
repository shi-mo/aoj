#include <iostream>
#include <deque>
using namespace std;

int main()
{
    int q, query;
    deque<long> deq;

    cin >> q;
    while (cin >> query) {
        int d;
        switch (query) {
        case 0:
            int x;
            cin >> d;
            cin >> x;
            if (d <= 0) {
                deq.push_front(x);
                break;
            }
            deq.push_back(x);
            break;
        case 1:
            int p;
            cin >> p;
            cout << deq[p] << endl;
            break;
        case 2:
            cin >> d;
            if (d <= 0) {
                deq.pop_front();
                break;
            }
            deq.pop_back();
        }
    }
}
