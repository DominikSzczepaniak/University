public class ListHelper
{
    public static List<TOutput> ConvertAll<T, TOutput>(List<T> list, Converter<T, TOutput> converter)
    {
        List<TOutput> outputList = new List<TOutput>();
        foreach (T item in list)
        {
            outputList.Add(converter(item));
        }

        return outputList;
    }
    public static List<T> FindAll<T>(List<T> list, Predicate<T> match)
    {
        List<T> outputList = new List<T>();
        foreach (var item in list)
        {
            if (match(item))
            {
                outputList.Add((item));
            }
        }
        return outputList;
    }

    public static void ForEach<T>(List<T> list, Action<T> action)
    {
        foreach (var item in list)
        {
            action(item);
        }
    }

    public static int RemoveAll<T>(List<T> list, Predicate<T> match)
    {
        int wynik = 0;
        for (int i = list.Count() - 1; i >= 0; i--)
        {
            if (match(list[i]))
            {
                wynik++;
                list.RemoveAt(i);
            }
            
        }

        return wynik;
    }

    public static void Sort<T>(List<T> list, Comparison<T> comparison)
    {
        T[] array = list.ToArray();
        Array.Sort(array, comparison);
        list.Clear();
        list.AddRange(array);
    }
    
}

class Program
{
    public static void Main()
    {
        List<int> l1 = new List<int>();
        for (int i = 10; i >= 0; i--)
        {
            l1.Add(i*10);
        }
        ListHelper.Sort(l1, (i, i1) => i.CompareTo(i1));
        foreach (var VARIABLE in l1)
        {
            Console.Write(VARIABLE + " ");
        }
        Console.WriteLine();

        ListHelper.RemoveAll(l1, delegate(int x) { return (x % 20 == 0); });
        foreach (var VARIABLE in l1)
        {
            Console.Write(VARIABLE + " ");
        }
        Console.WriteLine();
    }
}