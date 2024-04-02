using System;
using System.Collections.Generic;

public interface IGraph
{
    void AddVertex(string vertex);
    void AddEdge(string vertex1, string vertex2);
    bool AreAdjacent(string vertex1, string vertex2);
    IEnumerable<string> GetNeighbors(string vertex);
    void GenerateRandomGraph(int vertices, int edges);
    List<string> ShortestPath(string startVertex, string endVertex);
}