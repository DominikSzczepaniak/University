#include <climits>
#include <iostream>
#include <vector>

using namespace std;
#define endl "\n"
#define ll long long
const int MAXN = 100;
const int MAXW = 1e6;

struct Item
{
    int weight;
    int value;
};

struct Answer
{
    string odpowiedz;
    string wynik;
    string przedmioty;
};

bool maximize(ll one, ll two)
{
    return one > two;
}

bool minimize(ll one, ll two)
{
    return one < two;
}

Answer calculate(bool (*func)(ll, ll), ll limit, vector<Item> &items, ll n, ll W)
{
    vector<ll> dp(MAXW + 1, limit);
    vector<int> choice(MAXW + 1, -1);
    dp[0] = 0;

    for (int i = 0; i < n; ++i)
    {
        for (int w = items[i].weight; w <= W; ++w)
        {
            if (dp[w - items[i].weight] != limit)
            {
                ll newVal = dp[w - items[i].weight] + items[i].value;
                if (func(newVal, dp[w]))
                {
                    dp[w] = newVal;
                    choice[w] = i;
                }
            }
        }
    }
    string odpowiedz = "";
    string wynik = "";
    string przedmioty = "";

    if (dp[W] == limit)
    {
        odpowiedz = "NIE";
    }
    else
    {
        odpowiedz = "TAK";
        wynik = to_string(dp[W]);

        int itemsChosen[MAXN];
        for (int i = 0; i < n; i++)
        {
            itemsChosen[i] = 0;
        }

        int currentWeight = W;
        while (currentWeight > 0)
        {
            itemsChosen[choice[currentWeight]]++;
            currentWeight -= items[choice[currentWeight]].weight;
        }

        for (int i = 0; i < n; i++)
        {
            przedmioty += to_string(itemsChosen[i]) + " ";
        }
        przedmioty.pop_back();
    }

    return {odpowiedz, wynik, przedmioty};
}

int main()
{
    int W;
    int n;
    cin >> W;
    cin >> n;
    vector<Item> items(MAXN);
    for (int i = 0; i < n; i++)
    {
        cin >> items[i].value >> items[i].weight;
    }
    Answer one = calculate(maximize, -1, items, n, W);
    if (one.odpowiedz == "NIE")
    {
        cout << "NIE" << endl;
        return 0;
    }
    Answer two = calculate(minimize, LONG_LONG_MAX, items, n, W);
    if (two.odpowiedz == "NIE")
    {
        cout << "NIE" << endl;
        return 0;
    }
    cout << "TAK" << endl;
    cout << two.wynik << endl;
    cout << two.przedmioty << endl;
    cout << one.wynik << endl;
    cout << one.przedmioty << endl;
}
