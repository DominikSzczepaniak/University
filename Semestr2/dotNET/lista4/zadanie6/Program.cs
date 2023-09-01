//Rejestr zdarzeń serwera IIS ma postać pliku tekstowego, w którym każda linia ma postać:
//08:55:36 192.168.0.1 GET /TheApplication/WebResource.axd 200
//gdzie poszczególne wartości oznaczają czas, adres klienta, rodzaj żądania HTTP, nazwę zasobu oraz status odpowiedzi.
//Napisać aplikację która za pomocą jednego (lub wielu) wyrażeń LINQ wydobędzie z przy- kładowego rejestru zdarzeń
//IIS listę adresów IP trzech klientów, którzy skierowali do ser- wera aplikacji największą liczbę żądań.
//Wynikiem działania programu powinien być przykładowy raport postaci:
//12.34.56.78 143
//23.45.67.89 113
//123.245.167.289 89
//gdzie pierwsza kolumna oznacza adres klienta, a druga liczbę zarejestrowanych żądań.

class Program
{
    public static void Main()
    {
        var plik = File.ReadAllLines("rejestr.txt");
        var adresyIP =
            (from v in plik
            select v.Split(" ")[1]);
        foreach (var v in adresyIP.GroupBy(x => x).Select(group => new
                 {
                     IP = group.Key,
                     Amount = group.Count()
                 }).Take(3).OrderByDescending(x => x.Amount))
        {
            Console.WriteLine(v.IP + " " + v.Amount);
        }
    }
}