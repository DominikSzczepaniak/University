#include <iostream>
#include <fstream>
#include <memory>
#include <string>
using namespace std;

class LineWriter {
public:
    LineWriter(const string& filename) {
        file_stream = make_shared<ofstream>(filename, ios::out);
        if (!file_stream->is_open()) {
            cerr << "Failed to open the file: " << filename << endl;
        }
    }
    void writeLine(const string& line) {
        if (file_stream->is_open()) {
            (*file_stream) << line << endl;
        }
    }
    ~LineWriter() {
        if (file_stream && file_stream->is_open()) {
            file_stream->close();
            cout << "Zamknieto plik" << endl;
        }
    }
private:
    shared_ptr<ofstream> file_stream;
};

int main() {
    string filename = "output.txt";
    shared_ptr<LineWriter> writer1 = make_shared<LineWriter>(filename);
    shared_ptr<LineWriter> writer2 = writer1; 
    shared_ptr<LineWriter> writer3 = writer1; 
    writer1->writeLine("To jest pierwszy wiersz.");
    writer2->writeLine("To jest drugi wiersz.");
    writer3->writeLine("To jest trzeci wiersz.");    
    
    return 0;
}
