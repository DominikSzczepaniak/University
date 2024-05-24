#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int N = 500002;
const int K = 5002;

vector<int> g[N];
int n, k, sz[N], lvl[N];
int tot, done[N], cenpar[N], cnt[K];

void calc_sz(int u, int p)
{
    tot++;
    sz[u] = 1;
    for (auto v : g[u])
    {
        if (v == p || done[v])
        {
            continue;
        }
        calc_sz(v, u);
        sz[u] += sz[v];
    }
}
void dfs(int u, int p, int d, int val)
{
    cnt[d] += val;
    for (auto v : g[u])
    {
        if (v == p || done[v])
        {
            continue;
        }
        dfs(v, u, d + 1, val);
    }
}
long long res = 0;
void calc(int u, int p, int d)
{
    if (k - d > 0)
    {
        res += cnt[k - d];
    }
    for (auto v : g[u])
    {
        if (v == p || done[v])
        {
            continue;
        }
        calc(v, u, d + 1);
    }
}
int find_cen(int u, int p)
{
    for (auto v : g[u])
    {
        if (v == p || done[v])
        {
            continue;
        }
        else if (sz[v] > tot / 2)
        {
            return find_cen(v, u);
        }
    }
    return u;
}
void decompose(int u, int pre)
{
    tot = 0;
    calc_sz(u, pre);
    int cen = find_cen(u, pre);
    // calculating ans
    dfs(cen, pre, 0, 1);
    res += cnt[k];
    for (auto v : g[cen])
    {
        if (v == pre || done[v])
        {
            continue;
        }
        dfs(v, cen, 1, -1); //usuwamy dla poddrzewa zeby nie bylo sytuacji ze mamy d w tym samym poddrzewie co d-k. nie musimy liczyc spowrotem bo bysmy liczyli dla tego jednego poddrzewa podwojnie, wiec nie musimy robic /2.
        calc(v, cen, 1);
    }

    cenpar[cen] = pre;
    done[cen] = 1;
    for (auto v : g[cen])
    {
        if (v == pre || done[v])
        {
            continue;
        }
        decompose(v, cen);
    }
}
void solve()
{
    cin >> n >> k;
    for (int i = 1; i < n; i++)
    {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    decompose(1, 0);
    cout << res << '\n';
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); // cout.tie(NULL);
    solve();
    return 0;
}