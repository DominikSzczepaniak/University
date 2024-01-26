#include <iostream>
#include <thread>
#include <queue>
#include <condition_variable>
#include <chrono>
using namespace std;
queue<int> buffer;
const unsigned int buffer_size = 10;
mutex mtx;
condition_variable cv;

void producer(int id) {
    for (int i = 0; i < 50; ++i) {
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, []{ return buffer.size() < buffer_size; });
        buffer.push(i);
        cout << "Producer " << id << " produced " << i << endl;
        cv.notify_all();
        lock.unlock();
        this_thread::sleep_for(chrono::milliseconds(50));
    }
}

void consumer(int id) {
    for (int i = 0; i < 50; ++i) {
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, []{ return !buffer.empty(); });
        int val = buffer.front();
        buffer.pop();
        cout << "Consumer " << id << " consumed " << val << endl;
        cv.notify_all();
        lock.unlock();
        this_thread::sleep_for(chrono::milliseconds(50));
    }
}

int main() {
    thread producers[2];
    thread consumers[2];

    for (int i = 0; i < 2; ++i) {
        producers[i] = thread(producer, i + 1);
        consumers[i] = thread(consumer, i + 1);
    }

    for (int i = 0; i < 2; ++i) {
        producers[i].join();
        consumers[i].join();
    }

    return 0;
}