// Dominik Szczepaniak
using System.Collections;

public class SlowaFibonacciego : IEnumerable<string>
{
    private int _maxCount;

    public SlowaFibonacciego(int count)
    {
        _maxCount = count;
    }

    public IEnumerator<string> GetEnumerator()
    {
        string a = "b", b = "a";
        for (int i = 1; i <= _maxCount; i++)
        {
            if (i == 1) yield return a;
            else if (i == 2) yield return b;
            else
            {
                string temp = b + a;
                a = b;
                b = temp;
                yield return temp;
            }
        }
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }
}

class Program
{
    public static void Main()
    {
        SlowaFibonacciego sf = new SlowaFibonacciego(6);
        foreach (string s in sf)
        {
            Console.WriteLine(s);
        }
    }
}