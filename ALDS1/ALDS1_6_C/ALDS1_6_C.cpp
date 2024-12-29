#include <iostream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;

typedef pair<char,int> card_t;
typedef pair<int,int> range_t;
typedef function<int(card_t,card_t)> cmp_func;

void qsort(vector<card_t>& a, int p, int r, cmp_func cmp) {
    stack<range_t> stk;
    stk.push(make_pair(p,r));

    while (!stk.empty()) {
        int b, e, i;
        card_t x, tmp;
        range_t be;

        be = stk.top();
        stk.pop();
        b = be.first;
        e = be.second;
        x = a[e];
        i = b-1;

        if (e <= b) continue;
        for (int j = b; j < e; j++) {
            if (cmp(x, a[j])) continue;
            i++;
            tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
        }
        tmp = a[i+1];
        a[i+1] = a[e];
        a[e] = tmp;
        stk.push(make_pair(i+2,e));
        stk.push(make_pair(b,i));
    }
}

int main()
{
    int n;
    char c;
    vector<card_t> a;

    cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        int v;
        cin >> c;
        cin >> v;
        a[i] = make_pair(c, v);
    }
    qsort(a, 0, n-1, [](card_t a, card_t b){
            return a.second < b.second; });
    for (const auto& ai: a) {
        cout << ai.first << " " << ai.second << endl;
    }
    a.clear();
}
