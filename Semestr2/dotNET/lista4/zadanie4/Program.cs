//Napisać wyrażenie LINQ, które dla zadanego foldera wyznaczy sumę długości
//plików znajdujących się w tym folderze.
//Do zbudowania sumy długości plików użyć funkcji Aggregate. Listę plików w zadanym folderze wydobyć za
//pomocą odpowiednich metod z przestrzeni nazw System.IO.

using System.IO;
using System.IO.Enumeration;

class Program
{
    public static void Main()
    {
        var files = Directory.GetFiles("folder");
        int sum = 0;
        int FileLengthInFolder =
            (from fileName in files
                from line in File.ReadAllLines(fileName)
                select line.Length).Sum(x => x);
        Console.WriteLine(FileLengthInFolder);
    }
}