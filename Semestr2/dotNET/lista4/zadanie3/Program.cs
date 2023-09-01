//Dany jest plik tekstowy zawierający zbiór nazwisk w kolejnych liniach.
//Napisać wyrażenie LINQ, które zwróci zbiór pierwszych liter nazwisk uporządkowanych w kolejności alfabetycznej.
//Na przykład dla zbioru (Kowalski, Malinowski, Krasicki, Abac- ki) wynikiem powinien być zbiór (A, K, M).
string[] lines = File.ReadAllLines("input.txt");
var firstLetters =
    (from l in lines
        orderby l[0] ascending
        select l[0]).GroupBy(x => x);
foreach (var a in firstLetters)
{
    Console.WriteLine(a.Key);
}
    