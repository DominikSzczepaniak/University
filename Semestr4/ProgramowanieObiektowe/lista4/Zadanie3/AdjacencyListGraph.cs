using ArgumentException = System.ArgumentException;

namespace Zadanie3;

public class AdjacencyListGraph : IGraph
{
    private Dictionary<string, List<string>> adjacencyList;
    public AdjacencyListGraph()
    {
        adjacencyList = new Dictionary<string, List<string>>();
    }

    public void AddVertex(string vertex)
    {
        if (adjacencyList.ContainsKey(vertex))
        {
            throw new ArgumentException("vertex already exists");
        }
        adjacencyList[vertex] = new List<string>();
    }

    public void AddEdge(string vertex1, string vertex2)
    {
        if (!adjacencyList.ContainsKey(vertex1) || !adjacencyList.ContainsKey(vertex2))
        {
            throw new ArgumentException("vertices do not exist");
        }

        adjacencyList[vertex1].Add(vertex2);
        adjacencyList[vertex2].Add(vertex1);
    }

    public bool AreAdjacent(string vertex1, string vertex2)
    {
        if (!adjacencyList.ContainsKey(vertex1) || !adjacencyList.ContainsKey(vertex2))
        {
            throw new ArgumentException("vertices do not exist");
        }
        return adjacencyList.ContainsKey(vertex1) && adjacencyList[vertex1].Contains(vertex2);
    }

    public IEnumerable<string> GetNeighbors(string vertex)
    {
        if (!adjacencyList.ContainsKey(vertex))
        {
            throw new ArgumentException("vertex does not exist");
        }
        foreach (var neighbor in adjacencyList[vertex])
        {
            yield return neighbor;
        }
    }

    public void GenerateRandomGraph(int vertices, int edges)
    {
        adjacencyList.Clear();

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
        if (!adjacencyList.ContainsKey(startVertex) || !adjacencyList.ContainsKey(endVertex))
        {
            throw new ArgumentException("vertices do not exist");
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