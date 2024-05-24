#include <iostream>
#include <set>
#include <vector>

using namespace std;

constexpr long long MAX_VALUE = 1e18;

struct Line {
    mutable long long slope, y_intercept, position;
    int index;

    bool operator<(const Line& other) const {
        return slope < other.slope;
    }

    bool operator<(long long x) const {
        return position < x;
    }
};

struct LineContainer : multiset<Line, less<>> {
    static constexpr long long INFINITY_POS = MAX_VALUE * 4;

    long long division(long long numerator, long long denominator) {
        return numerator / denominator - ((numerator ^ denominator) < 0 && numerator % denominator);
    }

    bool intersect(iterator current, iterator next) {
        if (next == end()) {
            current->position = INFINITY_POS;
            return false;
        }
        if (current->slope == next->slope) {
            current->position = current->y_intercept > next->y_intercept ? INFINITY_POS : -INFINITY_POS;
        } else {
            current->position = division(next->y_intercept - current->y_intercept, current->slope - next->slope);
        }
        return current->position >= next->position;
    }

    void add(long long slope, long long y_intercept, int index) {
        auto it = insert({slope, y_intercept, 0, index}), next = it++, prev = next;
        while (intersect(next, it)) it = erase(it);
        if (prev != begin() && intersect(--prev, next)) intersect(prev, next = erase(next));
        while ((next = prev) != begin() && (--prev)->position >= next->position) intersect(prev, erase(next));
    }

    pair<long long, int> query(long long x) {
        auto l = *lower_bound(x);
        return {l.slope * x + l.y_intercept, l.index};
    }
};

int main() {
    int k, n;
    cin >> k >> n;

    vector<long long> freq(n + 1, 0);
    vector<long long> cumulativeFreq(n + 1, 0), weightedFreq(n + 1, 0);
    vector<vector<int>> answers(n + 1);
    vector<long long> dp(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        cin >> freq[i];
        cumulativeFreq[i] = cumulativeFreq[i - 1] + freq[i];
        weightedFreq[i] = weightedFreq[i - 1] + i * freq[i];
        dp[i] = weightedFreq[i];
        answers[i].push_back(i);
    }

    vector<long long> currentDP(n + 1, 0);
    vector<vector<int>> currentAnswers(n + 1);

    for (int partition = 2; partition <= k; ++partition) {
        LineContainer hull;
        hull.add(partition - 1, -(dp[partition - 1] - weightedFreq[partition - 1] + (partition - 1) * cumulativeFreq[partition - 1]), partition - 1);

        for (int i = partition; i <= n; ++i) {
            auto queryResult = hull.query(cumulativeFreq[i]);
            currentDP[i] = weightedFreq[i] - queryResult.first;
            currentAnswers[i] = answers[queryResult.second];
            currentAnswers[i].push_back(i - queryResult.second);
            hull.add(i, -(dp[i] - weightedFreq[i] + i * cumulativeFreq[i]), i);
        }
        swap(dp, currentDP);
        swap(answers, currentAnswers);
    }

    cout << dp[n] << endl;
    for (int num : answers[n]) {
        cout << num << " ";
    }
    cout << endl;
}
