#include <iostream>
#include <string>
#include <unordered_map>
#include <list>
#include <queue>
using namespace std;
class WeightedGraph {
private:
    unordered_map<string, list<pair<string, double>>> adjacencyList;

public:
    void addNode(const string& Node) {
        adjacencyList[Node]; 
    }

    void addEdge(const string& startNode, const string& endNode, double weight) {
        adjacencyList[startNode].push_back(make_pair(endNode, weight));
        adjacencyList[endNode].push_back(make_pair(startNode, weight));
    }

    void removeNode(const string& Node) {
        adjacencyList.erase(Node);
        for (auto& entry : adjacencyList) {
            entry.second.remove_if([Node](const auto& pair) { return pair.first == Node; });
        }
    }

    void removeEdge(const string& startNode, const string& endNode) {
        adjacencyList[startNode].remove_if([endNode](const auto& pair) { return pair.first == endNode; });
        adjacencyList[endNode].remove_if([startNode](const auto& pair) { return pair.first == startNode; });
    }

    void changeEdgeWeight(const string& startNode, const string& endNode, double newWeight) {
        for (auto& pair : adjacencyList[startNode]) {
            if (pair.first == endNode) {
                pair.second = newWeight;
                break;
            }
        }
        for (auto& pair : adjacencyList[endNode]) {
            if (pair.first == startNode) {
                pair.second = newWeight;
                break;
            }
        }
    }

    WeightedGraph findMSTPrim() {
        WeightedGraph mst; 
        unordered_map<string, bool> visited; 
        priority_queue<pair<double, pair<string, string>>> pq; 

        for (const auto& entry : adjacencyList) {
            visited[entry.first] = false;
        }

        visited[adjacencyList.begin()->first] = true;
        for (const auto& edge : adjacencyList[adjacencyList.begin()->first]) {
            pq.push(make_pair(-edge.second, make_pair(adjacencyList.begin()->first, edge.first)));
        }
        

        while (!pq.empty()) {
            auto edge = pq.top();
            pq.pop();

            double weight = -edge.first;
            string startNode = edge.second.first;
            string endNode = edge.second.second;

            if (!visited[endNode]) {
                mst.addNode(endNode);
                mst.addEdge(startNode, endNode, weight);
                visited[endNode] = true;

                for (const auto& newEdge : adjacencyList[endNode]) {
                    pq.push(make_pair(-newEdge.second, make_pair(endNode, newEdge.first)));
                }
            }
        }

        return mst;
    }

    void printGraph() const {
        for (const auto& entry : adjacencyList) {
            cout << "Node " << entry.first << ": ";
            for (const auto& edge : entry.second) {
                cout << "(" << edge.first << ", " << edge.second << ") ";
            }
            cout << endl;
        }
    }
};

int main() {
    WeightedGraph graph;

    graph.addNode("A");
    graph.addNode("B");
    graph.addNode("C");
    graph.addNode("D");
    graph.addNode("E");
    graph.addNode("F");

    graph.addEdge("A", "B", 2.0);
    graph.addEdge("B", "C", 1.5);
    graph.addEdge("A", "C", 3.0);
    graph.addEdge("C", "D", 1.0);
    graph.addEdge("D", "E", 2.0);
    graph.addEdge("E", "F", 3.0);
    graph.addEdge("D", "F", 1.0);
    graph.addEdge("A", "F", 4.0);   
    graph.addEdge("B", "F", 3.0);
    graph.addEdge("C", "F", 2.0);

    WeightedGraph mst = graph.findMSTPrim();
    mst.printGraph();
    return 0;

//https://csacademy.com/app/graph_editor/
// A B 2
// B C 1.5
// A C 3.0
// C D 1.0
// D E 2.0
// E F 3.0
// D F 1.0
// A F 4.0
// B F 3.0
// C F 2.0
//out:
// A B 2
// B C 1.5
// C D 1
// D E 2
// D F 1

}
