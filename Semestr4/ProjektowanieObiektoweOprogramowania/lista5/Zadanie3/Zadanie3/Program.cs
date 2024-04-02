using System;
using System.Collections;

class Program
{
    private class ComparerWrapper<T> : IComparer
    {
        private readonly Comparison<T> _comparison;

        public ComparerWrapper(Comparison<T> comparison)
        {
            _comparison = comparison;
        }
        
        public int Compare(object x, object y)
        {
            return _comparison((T)x, (T)y);
        }
    }
    
    static int IntComparer(int x, int y)
    {
        return x.CompareTo(y);
    }

    static void Main(string[] args)
    {
        ArrayList a = new ArrayList() { 1, 5, 3, 3, 2, 4, 3 };
        a.Sort(new ComparerWrapper<int>(IntComparer));
        foreach (int item in a)
        {
            Console.WriteLine(item);
        }
        Console.ReadLine();
    }
}