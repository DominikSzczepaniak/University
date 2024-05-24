#include <bits/stdc++.h>

using namespace std;

struct Line
{
    mutable long long k, m, p, idx;
    bool operator<(const Line &o) const { return k < o.k; }
    bool operator<(long long x) const { return p < x; }
};
constexpr long long M = (long long)1e18;

struct LineContainer : multiset<Line, less<>>
{
    static constexpr long long inf = M*4;
    long long div(long long a, long long b)
    {
        return a / b - ((a ^ b) < 0 && a % b);
    }
    bool isect(iterator x, iterator y)
    {
        if (y == end())
            return x->p = inf, 0;
        if (x->k == y->k)
            x->p = x->m > y->m ? inf : -inf;
        else
            x->p = div(y->m - x->m, x->k - y->k);
        return x->p >= y->p;
    }
    void add(long long k, long long m, int idx)
    {
        auto z = insert({k, m, 0, idx}), y = z++, x = y;
        while (isect(y, z))
            z = erase(z);
        if (x != begin() && isect(--x, y))
            isect(x, y = erase(y));
        while ((y = x) != begin() && (--x)->p >= y->p)
            isect(x, erase(y));
    }
    pair<long long, int> query(long long x)
    {
        auto l = *lower_bound(x);
        return {l.k * x + l.m, l.idx};
    }
};

int main()
{
    int n, k;
    cin >> k >> n;

    vector<long long> freq(n + 1);
    vector<long long> A(n + 1, 0), B(n + 1, 0);
    long long dp[2][10001];
    vector<vector<vector<int>>> answers(2, vector<vector<int>>(n+1));
    for (int i = 1; i <= n; ++i) {
        cin >> freq[i];
        A[i] = A[i - 1] + freq[i];
        B[i] = B[i - 1] + i * freq[i];
        dp[1][i] = B[i];
        answers[1][i] = {i};
    }

    int last_chosen = 0;    
    for (int ki = 2; ki <= k; ki++)
    {
        int current = ki%2;
        int prev = 1 - current;
        last_chosen = current;
        LineContainer cht;
        cht.add(ki-1, -(dp[prev][ki-1]-B[ki-1]+(ki-1)*A[ki-1]), ki-1);

        for (int i = ki; i <= n; i++)
        {
            // m dajemy dodatni
            // c dajemy ujemne 
            // dajemy + B[i]
            // odejmujemy eval dla otoczki
            pair<long long, int> p = cht.query(A[i]);
            dp[current][i]=B[i] - p.first;
            answers[current][i] = answers[prev][p.second];
            answers[current][i].push_back(i-p.second);
            cht.add(i,-(dp[prev][i] - B[i] + i*A[i]), i);
            
        }
    }

    cout << dp[last_chosen][n] << endl;
    for (auto num : answers[last_chosen][n]) {
        cout << num << " ";
    }
    cout << endl;
}