#include <iostream>
#include <list>
using namespace std;

int main()
{
    int q, query;
    list<long> lst;
    auto cursor = lst.begin();

    cin >> q;
    while (cin >> query) {
        switch (query) {
        case 0: // insert x
            int x;
            cin >> x;
            cursor = lst.insert(cursor, x);
            break;
        case 1: // move d
            int d;
            cin >> d;
            if (0 < d) {
                for (int i = 0; i < d; i++) cursor++;
                break;
            }
            for (int i = 0; i < -d; i++) cursor--;
            break;
        case 2: // erase
            cursor = lst.erase(cursor);
        }
    }

    for(cursor = lst.begin(); lst.end() != cursor; cursor++) {
        cout << *cursor << endl;
    }
}
