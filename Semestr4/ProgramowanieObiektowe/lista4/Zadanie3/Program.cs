// Dominik Szczepaniak
using System.Runtime.InteropServices;
using Zadanie3;

class Program
{
    public static void Main()
    {
        MatrixGraph mg = new MatrixGraph();
        mg.GenerateRandomGraph(10, 15);
        var list = mg.ShortestPath("V1", "V10");
        foreach (var s in list)
        {
            Console.Write(s + " ");
        }
        Console.WriteLine();
        AdjacencyListGraph alg = new AdjacencyListGraph();
        alg.GenerateRandomGraph(10, 13); 
        var list2 = alg.ShortestPath("V1", "V10");
        //nie mam za bardzo wypływu na to jak wylosuje, więc może dać pustą ścieżkę lub jakąś krótką
        foreach (var s in list2)
        {
            Console.Write(s + " ");
        }
        Console.WriteLine();
        Console.WriteLine();
        Console.WriteLine();
        alg = new AdjacencyListGraph();
        alg.AddVertex("V1");
        alg.AddVertex("V2");
        alg.AddVertex("V3");
        alg.AddVertex("V4");
        alg.AddVertex("V5");
        alg.AddVertex("V6");
        alg.AddVertex("V7");
        alg.AddVertex("V8");
        alg.AddVertex("V9");
        alg.AddVertex("V10");
        alg.AddEdge("V1", "V2");
        alg.AddEdge("V1", "V3");
        alg.AddEdge("V2", "V4");
        alg.AddEdge("V2", "V5");
        alg.AddEdge("V2", "V6");
        alg.AddEdge("V3", "V7");
        alg.AddEdge("V6", "V8");
        alg.AddEdge("V6", "V9");
        alg.AddEdge("V9", "V10");
        //          V1
        //     V2           V3 
        // V4  V5    V6        V7
        //        |V8  V9
        //               V10
        Console.WriteLine(alg.AreAdjacent("V1", "V3"));
        Console.WriteLine(alg.AreAdjacent("V1", "V10"));
        foreach (var s in alg.ShortestPath("V1", "V10"))
        {
            Console.Write(s + " ");
        }
        Console.WriteLine();


        AdjacencyListGraph errorGraph = new AdjacencyListGraph();
        try
        {
            errorGraph.AddEdge("V1", "V2");
        }
        catch (ArgumentException e)
        {
            Console.WriteLine(e);
        }
        errorGraph.AddVertex("V1");
        try
        {
            errorGraph.AddVertex("V1");
        }
        catch (ArgumentException e)
        {
            Console.WriteLine(e);
        }
        try
        {
            errorGraph.AreAdjacent("V1", "V100");
        }
        catch (ArgumentException e)
        {
            Console.WriteLine(e);
        }
        

    }
}