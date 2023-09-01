class Program
{
    public static void Main()
    {
        List<int> list = new List<int>();
        for (int i = 0; i < 20; i++)
        {
            list.Add(4*i);
        }
        var listTimesTwo = list.ConvertAll(delegate(int x) { return 2 * x;});
        var listFindDivisibleByEight = list.FindAll(delegate(int x) { return (x % 8 == 0);});
        list.ForEach(delegate(int x) { Console.Write(x + " "); });
        Console.WriteLine();
        foreach (var i in listTimesTwo)
        {
            Console.Write(i + " ");
        }
        Console.WriteLine();
        foreach (var i in listFindDivisibleByEight)
        {
            Console.Write(i + " ");
        }
        Console.WriteLine();
        var test = list.RemoveAll(delegate(int x) { return x % 16 == 0; });
        Console.WriteLine("REMOVEALL: " + test);
        foreach (var i in list)
        {
            Console.Write(i + " ");
        }
        Console.WriteLine();
        list.Sort(delegate(int x, int y) { return y.CompareTo(x); });
        foreach (var i in list)
        {
            Console.Write(i + " ");
        }
        Console.WriteLine();
    }
}