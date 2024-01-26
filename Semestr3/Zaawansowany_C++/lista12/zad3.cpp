#include <thread>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
void merge(vector<int>& arr, int low, int mid, int high) {
    vector<int> left(arr.begin() + low, arr.begin() + mid + 1);
    vector<int> right(arr.begin() + mid + 1, arr.begin() + high + 1);

    int i = 0, j = 0, k = low;
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) {
            arr[k++] = left[i++];
        } else {
            arr[k++] = right[j++];
        }
    }

    while (i < left.size()) {
        arr[k++] = left[i++];
    }

    while (j < right.size()) {
        arr[k++] = right[j++];
    }
}

void merge_sort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int mid = low + (high - low) / 2;

        thread left_sort(merge_sort, ref(arr), low, mid);
        thread right_sort(merge_sort, ref(arr), mid + 1, high);

        left_sort.join();
        right_sort.join();

        merge(arr, low, mid, high);
    }
}

int main() {
    vector<int> arr = {10, 5, 2, 3, 8, 6, 1, 13, 11, 12, 9, 4, 7, 15, 17, 18, 16, 19, 20};
    merge_sort(arr, 0, arr.size() - 1);

    for (int num : arr) {
        cout << num << " ";
    }

    return 0;
}