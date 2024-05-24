#include <iostream>
#include <vector>
#include <deque>
#include <limits>
#include <map>
using namespace std;
struct Line {
    long long m, c; 
    long long idx; 
};

long long getY(const Line& line, long long x) {
    return line.m * x + line.c;
}

long long calculate_cost(int l, int r, const vector<long long>& A, const vector<long long>& B) {
    return B[r] - B[l-1] - (l-1) * (A[r] - A[l-1]);
} //DOBRZE

int main() {
    long long K, L;
    std::cin >> K >> L;

    std::vector<long long> freq(L + 1), A(L + 1), B(L + 1);
    std::vector<std::vector<long long>> dp(K + 1, std::vector<long long>(L + 1));
    vector<vector<vector<int>>> answer(K + 1, vector<vector<int>>(L + 1));
    std::deque<Line> hull;

    for (int i = 1; i <= L; ++i) {
        cin >> freq[i];
        A[i] = A[i - 1] + freq[i];
        B[i] = B[i - 1] + i * freq[i];
    }

 ///DOBRZE
    dp[1][0] = 0;
    for (long long j = 1; j <= L; ++j) {
        dp[1][j] = calculate_cost(1, j, A, B);
        answer[1][j] = {int(j)};
    }
    int previous = 0;
    for (long long k = 2; k <= K; ++k) {
        hull.clear();
        hull.push_back({-(k-1), dp[k-1][k-1] - B[k-1] + (k-1)*A[k-1], k-1});

        for (long long j = k; j <= L; ++j) {
            
            while (hull.size() >= 2 && getY(hull.front(), A[j]) + B[j] > getY(hull[1], A[j]) + B[j]){
                hull.pop_front();
            }
            dp[k][j] = getY(hull.front(), A[j]) + B[j];
            answer[k][j] = answer[k-1][hull.front().idx];
            answer[k][j].push_back(j - hull.front().idx);
            Line newLine = {-j, dp[k - 1][j] - B[j] + j*A[j], j};
            while (hull.size() >= 1 && getY(newLine, A[j+1]) + B[j+1] < getY(hull.back(), A[j+1]) + B[j+1]) {
                hull.pop_back();
            }

            hull.push_back(newLine);
        }
    }
    // for(int i = 1; i<=K; i++){
    //     for(int j = 1; j<=L; j++){
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    std::cout << dp[K][L] << std::endl;
    for (auto num : answer[K][L]) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}
