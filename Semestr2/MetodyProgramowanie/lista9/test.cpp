// you can use includes, for example:
#include <algorithm>
#include <vector>
#include <bits/stdc++.h>
#include <string>

using namespace std;
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(string &S) {
    int n = S.length();
    vector<int> arr(n);
    for(int i = 0; i<n; i++){
        arr[i] = S[i] - 'a';
    }
    vector<int> sequence(n, 0);
    int answer = 1;
    sequence[0] = arr[0];
    for(int i = 1; i<n; i++){
        if(arr[i] < sequence[0]){
            sequence[0] = arr[i];
        }
        else if(arr[i] > sequence[answer-1]){
            answer++;
            sequence[answer] = arr[i];
        }
        else{
            int start = -1;
            int end = answer - 1;
            while(start < end){
                int mid = (start + (start-end)) / 2;
                if(arr[mid] >= arr[i]){
                    end = mid;
                }
                else{
                    start = mid;
                }
            }
            sequence[end] = arr[i];
        }
    }
    return n - answer;
}

int main(){
    string S = "banana";
    cout << solution(S);
}

