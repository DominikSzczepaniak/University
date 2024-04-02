using System;
using System.Collections.Generic;
using System.Linq;
namespace Zadanie3;

public class MatrixGraph : IGraph
{
    private Dictionary<string, int> vertexIndices;
    private bool[,] adjacencyMatrix;
    private int verticesCount;
    
    public MatrixGraph()
    {
        vertexIndices = new Dictionary<string, int>();
        verticesCount = 0;
        adjacencyMatrix = new bool[0, 0];
    }

    public void AddVertex(string vertex)
    {
        if (vertexIndices.ContainsKey(vertex))
        {
            throw new ArgumentException("vertex already exists");
        }
        vertexIndices.Add(vertex, verticesCount);
        verticesCount++;
        
        bool[,] newAdjacencyMatrix = new bool[verticesCount, verticesCount];
        for (int i = 0; i < verticesCount - 1; i++)
        {
            for (int j = 0; j < verticesCount - 1; j++)
            {
                newAdjacencyMatrix[i, j] = adjacencyMatrix[i, j];
            }
        }
        adjacencyMatrix = newAdjacencyMatrix;

    }

    public void AddEdge(string vertex1, string vertex2)
    {
        if (!vertexIndices.ContainsKey(vertex1) || !vertexIndices.ContainsKey(vertex2))
        {
            throw new ArgumentException("vertices do not exist");
        }
        int id1 = vertexIndices[vertex1];
        int id2 = vertexIndices[vertex2];
        adjacencyMatrix[id1, id2] = true;
        adjacencyMatrix[id2, id1] = true;
    }

    public bool AreAdjacent(string vertex1, string vertex2)
    {
        if (!vertexIndices.ContainsKey(vertex1) || !vertexIndices.ContainsKey(vertex2))
        {
            throw new ArgumentException("vertices do not exist");
        }
        int id1 = vertexIndices[vertex1];
        int id2 = vertexIndices[vertex2];
        return adjacencyMatrix[id1, id2];
    }

    public IEnumerable<string> GetNeighbors(string vertex)
    {
        if (!vertexIndices.ContainsKey(vertex))
        {
            throw new ArgumentException("vertex does not exist");
        }

        int vertexIndex = vertexIndices[vertex];
        for (int i = 0; i < verticesCount; i++)
        {
            if (adjacencyMatrix[vertexIndex, i])
            {
                foreach (var kvp in vertexIndices)
                {
                    if (kvp.Value == i)
                    {
                        yield return kvp.Key;
                        break;
                    }
                }
            }
        }
    }

    public void GenerateRandomGraph(int vertices, int edges)
    {
        this.vertexIndices.Clear();
        this.adjacencyMatrix = new bool[vertices, vertices];
        this.verticesCount = 0;

        for (int i = 0; i < vertices; i++)
        {
            AddVertex("V" + (i + 1));
        }

        Random rnd = new Random();
        int maxEdges = vertices * (vertices - 1) / 2;
        edges = Math.Min(edges, maxEdges);

        while (edges > 0)
        {
            string vertex1 = "V" + rnd.Next(1, vertices + 1);
            string vertex2 = "V" + rnd.Next(1, vertices + 1);
            if (vertex1 != vertex2 && !AreAdjacent(vertex1, vertex2))
            {
                AddEdge(vertex1, vertex2);
                edges--;
            }
        }
    }

    public List<string> ShortestPath(string startVertex, string endVertex)
    {
        if (!vertexIndices.ContainsKey(startVertex) || !vertexIndices.ContainsKey(endVertex))
        {
            throw new ArgumentException("one of vertices does not exist");
        }

        var predecessors = new Dictionary<string, string>();
        var visited = new HashSet<string>();
        var queue = new Queue<string>();

        queue.Enqueue(startVertex);
        visited.Add(startVertex);

        while (queue.Count > 0)
        {
            var current = queue.Dequeue();
            foreach (var neighbor in GetNeighbors(current))
            {
                if (!visited.Contains(neighbor))
                {
                    visited.Add(neighbor);
                    predecessors[neighbor] = current;
                    queue.Enqueue(neighbor);

                    if (neighbor == endVertex)
                    {
                        var path = new List<string>();
                        for (var step = endVertex; step != null; step = predecessors.ContainsKey(step) ? predecessors[step] : null)
                        {
                            path.Insert(0, step);
                        }
                        return path;
                    }
                }
            }
        }

        return new List<string>();
    }
}