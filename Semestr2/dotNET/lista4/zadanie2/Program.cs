//Dany jest plik tekstowy zawierający zbiór liczb naturalnych w kolejnych liniach.
//Napisać wyrażenie LINQ, które odczyta kolejne liczby z pliku i wypisze tylko liczby większe niż 100,
//posortowane malejąco.
//from liczba in [liczby]
//  where ...
//  orderby ...
//  select ...
//Przeformułować wyrażenie LINQ na ciąg wywołań metod LINQ to Objects:
//[liczby].Where( ... ).OrderBy( ... )

using System.Collections;
using System.Reflection;

class Program
{
    public static void Main()
    {
        string[] lines = File.ReadAllLines("liczby.txt");
        List<int> liczby = new List<int>();
        foreach (var l in lines)
        {  
             liczby.Add(int.Parse(l));
        }
        IEnumerable<int> linesQuery =
            from l in liczby
            where l > 100
            orderby l descending 
            select l;
        var LINQToObjects = liczby.Where(x => x > 100).OrderByDescending(x=>x);
        //czym sie roznia? where w linq to wyrazenie logiczne, a w LINQ to object to Func<T, bool> 
        //co to orderby - w LINQ musimy podac IEnumerable wartosc ktora sortujemy, a pozniej Func<T, bool> do sortowania
        //w LINQtoObj podajemy Func<T, bool> (lambda) a pozniej comparator.
        
    }
}