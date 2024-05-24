#include <iostream>
#include <vector>
#include <limits>

using namespace std;

#define LLONG_MAX 922337203685477580

long long calculate_cost(int l, int r, const vector<long long>& A, const vector<long long>& B) {
    return B[r] - (l > 0 ? B[l-1] : 0) - (l > 0 ? (l-1) * (A[r] - A[l-1]) : 0);
}

int main() {
    long long K, L;
    cin >> K >> L;

    vector<long long> freq(L + 1), A(L + 1), B(L + 1);
    vector<vector<long long>> dp(2, vector<long long>(L + 1, LLONG_MAX));
    vector<vector<vector<int>>> choice(2, vector<vector<int>>(L + 1));

    for (int i = 1; i <= L; ++i) {
        cin >> freq[i];
        A[i] = A[i - 1] + freq[i];
        B[i] = B[i - 1] + i * freq[i];
    }
    int where = 1;
    if (K % 2 == 0){
        where = 0;
    }
    for (int l = 1; l <= L; ++l) {
        dp[where][l] = calculate_cost(l, L, A, B);
        choice[where][l].push_back(L - l + 1);  
    }


    int last_edited = 0;
    for (int k = K-1; k >= 1; --k) {
        int modulod = k % 2;
        last_edited = modulod;
        int prev = 1 - modulod;
        for (int l = L; l >= k; --l) {
            int skad = 0;
            for (int x = l + 1; x <= L; ++x) {
                long long cost = calculate_cost(l, x-1, A, B) + dp[prev][x];
                if (cost < dp[modulod][l]) {
                    skad = x;
                    dp[modulod][l] = cost;
                    choice[modulod][l] = choice[prev][x];
                    choice[modulod][l].insert(choice[modulod][l].begin(), x - l);
                }
            }
            // cout << "Dla k = " << k << " i l = " << l << " bierzemy z pola " << skad << endl;
            // cout << dp[modulod][l] << " ";
        }
        // cout << endl;
    }

    cout << dp[last_edited][1] << endl;
    for (auto num : choice[last_edited][1]) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
