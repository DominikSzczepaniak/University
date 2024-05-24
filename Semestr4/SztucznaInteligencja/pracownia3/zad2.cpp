#include <algorithm>
#include <fstream>
#include <functional>
#include <iostream>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

tuple<int, int, vector<vector<int>>, vector<vector<int>>, vector<set<vector<int>>>, vector<set<vector<int>>>>
input_data()
{
    ifstream file("zad_input.txt");
    int n, m;
    file >> n >> m;

    vector<vector<int>> row_val;
    vector<vector<int>> col_val;

    string line;
    getline(file, line);
    for (int i = 0; i < n; ++i)
    {
        getline(file, line);
        istringstream iss(line);
        vector<int> row;
        int num;
        while (iss >> num)
        {
            row.push_back(num);
        }
        row_val.push_back(row);
    }

    for (int i = 0; i < m; ++i)
    {
        getline(file, line);
        istringstream iss(line);
        vector<int> col;
        int num;
        while (iss >> num)
        {
            col.push_back(num);
        }
        col_val.push_back(col);
    }
    getline(file, line);
    vector<set<vector<int>>> row_domains;
    for (int i = 0; i < n; i++)
    {
        getline(file, line);
        set<vector<int>> row_domain;
        while (line != "NewRow")
        {
            istringstream iss(line);
            int num;
            vector<int> row;
            while (iss >> num)
            {
                row.push_back(num);
            }
            row_domain.insert(row);
            getline(file, line);
        }
        row_domains.push_back(row_domain);
    }
    vector<set<vector<int>>> col_domains;
    for (int i = 0; i < m; i++)
    {
        getline(file, line);

        set<vector<int>> col_domain;
        while (line != "NewRow")
        {
            istringstream iss(line);
            int num;
            vector<int> col;
            while (iss >> num)
            {
                col.push_back(num);
            }
            col_domain.insert(col);
            getline(file, line);
        }
        col_domains.push_back(col_domain);
    }

    return {n, m, row_val, col_val, row_domains, col_domains};
}

class Nonogram
{
  public:
    int n, m;
    vector<vector<int>> row_val;
    vector<vector<int>> col_val;
    vector<set<vector<int>>> row_domains;
    vector<set<vector<int>>> col_domains;

    Nonogram(
        tuple<int, int, vector<vector<int>>, vector<vector<int>>, vector<set<vector<int>>>, vector<set<vector<int>>>>
            data)
    {
        tie(n, m, row_val, col_val, row_domains, col_domains) = data;
    }
};

class MyAC3
{
  public:
    MyAC3(Nonogram nonogram)
    {
        solve(nonogram);
    }

    tuple<vector<set<vector<int>>>, vector<set<vector<int>>>> solve(Nonogram &nonogram)
    {
        // X - numery wierszow i kolumn
        // D - odpowiednie domeny
        queue<pair<pair<int, char>, pair<int, char>>> worklist;
        for (int i = 0; i < nonogram.n; i++)
        {
            for (int j = 0; j < nonogram.m; j++)
            {
                worklist.push({{i, 'r'}, {j, 'c'}});
                worklist.push({{j, 'c'}, {i, 'r'}});
            }
        }
        while (!worklist.empty())
        {
            auto arc = worklist.front();
            worklist.pop();
            auto x = arc.first;
            auto y = arc.second;
            if (x.second == 'r')
            {
                if (arc_reduce(x, y, nonogram.row_domains, nonogram.col_domains))
                {
                    if (nonogram.row_domains[x.first].empty())
                    {
                        return {nonogram.row_domains, nonogram.col_domains};
                    }
                    for (int i = 0; i < nonogram.m; i++)
                    {
                        if(i == y.first) continue;
                        worklist.push({{i, 'c'}, {x.first, 'r'}});
                    }
                }
            }
            else
            {
                if (arc_reduce(x, y, nonogram.col_domains, nonogram.row_domains))
                {
                    if (nonogram.col_domains[x.first].empty())
                    {
                        return {nonogram.row_domains, nonogram.col_domains};
                    }
                    for (int i = 0; i < nonogram.n; i++)
                    {
                        if(i == y.first) continue;
                        worklist.push({{i, 'r'}, {x.first, 'c'}});
                    }
                }
            }
        }
        return {nonogram.row_domains, nonogram.col_domains};
    }

  private:
    bool arc_reduce(pair<int, char> x, pair<int, char> y, vector<set<vector<int>>> &Dx, vector<set<vector<int>>> &Dy)
    {
        bool change = false;
        for(auto it = Dx[x.first].begin(); it != Dx[x.first].end();)
        {   
            bool satisfied = false;
            for(auto y_val : Dy[y.first])
            {
                if((*it)[y.first] == y_val[x.first]){
                    satisfied = true;
                    break;
                }
            }
            if(!satisfied)
            {
                it = Dx[x.first].erase(it);
                change = true;
            }
            else{
                it++;
            }
        }
        return change;
    }
};

class NonogramSolver
{
  public:
    vector<vector<int>> solution;

    // NonogramSolver(Nonogram &nonogram) : nonogram(nonogram) {
    //     solution = vector<vector<int>>(nonogram.n, vector<int>(nonogram.m, 0));
    // }

    NonogramSolver(Nonogram &nonogram)
    {
        solution = vector<vector<int>>(nonogram.n, vector<int>(nonogram.m, 0));
    }

    bool solve(Nonogram& nonogram)
    {
        return solve_row(0, nonogram);
    }

  private:
    // Nonogram& nonogram;

    bool solve_row(int row, Nonogram nonogram){
        MyAC3 ac3(nonogram);
        auto [row_domains, col_domains] = ac3.solve(nonogram);
        nonogram.row_domains = row_domains;
        nonogram.col_domains = col_domains;
        //every time calculate new domains
        if(row == nonogram.n){
            return true; //jesli tu doszlismy to musi byc okej bo inaczej by nie bylo dizedziny dla wiersza
        }
        for(auto it = nonogram.row_domains[row].rbegin(); it != nonogram.row_domains[row].rend(); it++){
        // for(auto row_config : nonogram.row_domains[row]){
            auto row_config = *it;
            vector<int> row_copy = solution[row];
            solution[row] = row_config;
            bool valid = true;
            vector<set<vector<int>>> col_domains_copy = nonogram.col_domains;
            for(int col = 0; col < nonogram.m; col++){
                updateDomains(row, nonogram.col_domains[col], solution[row][col]);
            }
            //check for empty domain:
            if (is_empty_domain(nonogram.col_domains) ){
                valid = false;
            }

            if(valid && solve_row(row + 1, nonogram)){
                return true;
            }
            nonogram.col_domains = col_domains_copy;
            solution[row] = row_copy;
        }
        return false;
    }

    void updateDomains(int rowNumber, set<vector<int>>& domain, int value){
        for(auto it = domain.begin(); it != domain.end();){
            if((*it)[rowNumber] != value){
                it = domain.erase(it);
            }
            else{
                it++;
            }
        }
    }

    bool is_empty_domain(vector<set<vector<int>>>& domains){
        for(auto domain : domains){
            if(domain.empty()){
                return true;
            }
        }
        return false;
    }
};

void save_to_file(vector<vector<int>> coloring)
{
    ofstream file("zad_output.txt");
    for (auto row : coloring)
    {
        for (int cell : row)
        {
            file << (cell == 0 ? '.' : '#');
        }
        file << endl;
    }
}

int main()
{
    Nonogram nonogram = Nonogram(input_data());

    NonogramSolver solver(nonogram);
    if (solver.solve(nonogram))
    {
        save_to_file(solver.solution);
        cout << "Nonogram solved successfully!" << endl;
    }
    else
    {
        cout << "No solution found." << endl;
    }

    return 0;
}
