namespace Zadanie4i5;

using System;
using System.Linq;
using System.Collections.Generic;
using Neo4j.Driver;

public class Zadanie4 : IDisposable
{
    private readonly IDriver _driver;

    public Zadanie4(string uri, string user, string password)
    {
        _driver = GraphDatabase.Driver(uri, AuthTokens.Basic(user, password));
    }

    public void PrintPersons()
    {
        using var session = _driver.Session();
        var persons = session.ExecuteRead(
            tx =>
            {
                var result = tx.Run("MATCH (p:Person) RETURN p.name AS name");
                return result.ToList();
            });

        Console.WriteLine("+----------------+");
        Console.WriteLine("|      Name      |");
        Console.WriteLine("+----------------+");

        foreach (var person in persons)
        {
            Console.WriteLine($"| {person["name"],-14} |");
        }

        Console.WriteLine("+----------------+");
    }

    public void Dispose()
    {
        _driver?.Dispose();
    }
}