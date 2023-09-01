//Dane są dwa pliki tekstowe, pierwszy zawierający zbiór danych osobowych postaci
//(Imię, Nazwisko, PESEL), drugi postaci (PESEL, NumerKonta). Kolejność danych w zbiorach jest przypadkowa.
//Napisać wyrażenie LINQ, które połączy oba zbiory danych i zbuduje zbiór danych zawierający
//rekordy postaci (Imię, Nazwisko, PESEL, NumerKonta). Do połączenia danych należy użyć operatora join.

using System.IO;
using System.Reflection.Metadata;

class Program
{
    public static void Main()
    {
        var plik1 = File.ReadAllLines("input1.txt");
        var plik2 = File.ReadAllLines("input2.txt");
        var answerFile =
            from wiersz1 in plik1
            join wiersz2 in plik2 on wiersz1.Split()[2] equals wiersz2.Split()[0]
            select wiersz1 + " " + wiersz2.Split()[1];

        foreach (var v in answerFile)
        {
            Console.WriteLine(v);
        }


    }
}