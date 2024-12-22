using System;
using System.Collections.Generic;
using System.Linq;
using Neo4j.Driver;

public class Person
{
    public string Name { get; set; }
    public override string ToString() => $"Name: {Name}";
}

public class MoviesPlayedin
{
    public List<string> Movies { get; set; }

    public override string ToString()
    {
        string result = "";
        Movies.ForEach(movie => result += movie.ToString() + " ");
        return result;
    }
}

public class Zadanie5 : IDisposable
{
    private readonly IDriver _driver;

    public Zadanie5(string uri, string user, string password)
    {
        _driver = GraphDatabase.Driver(uri, AuthTokens.Basic(user, password));
    }

    public void CreatePerson(string name)
    {
        using var session = _driver.Session();
        session.ExecuteWrite<object>(tx =>
        {
            tx.Run("CREATE (p:Person {name: $name})", new { name});
            return null;
        });
        Console.WriteLine($"Created person: {name}");
    }

    public void UpdatePerson(string name, string newName)
    {
        using var session = _driver.Session();
        session.ExecuteWrite<object>(tx =>
        {
            tx.Run("MATCH (p:Person {name: $name}) SET p.name = $newName", new { name, newName });
            return null;
        });
        Console.WriteLine($"Updated persons name: {name} to new name: {newName}");
    }

    public void DeletePerson(string name)
    {
        using var session = _driver.Session();
        session.ExecuteWrite<object>(tx =>
        {
            tx.Run("MATCH (p:Person {name: $name}) DETACH DELETE p", new { name });
            return null;
        });
        Console.WriteLine($"Deleted person: {name}");
    }

    public List<(Person person, MoviesPlayedin relationship)> GetPersonsWithRelationships()
    {
        using var session = _driver.Session();
        var result = session.ExecuteRead(tx =>
        {
            var query = @"
                MATCH (p:Person)-[r:ACTED_IN]->(n:Movie)
                RETURN p, collect(n.title) AS movies";

            return tx.Run(query).Select(record =>
            {
                var personNode = record["p"].As<INode>();
                var person = new Person
                {
                    Name = personNode.Properties["name"].As<string>()
                };

                var movies = record["movies"].As<List<object>>()
                    .Select(movie => movie.ToString())
                    .ToList();

                var relationship = new MoviesPlayedin
                {
                    Movies = movies
                };

                return (person, relationship);
            }).ToList();
        });

        return result;
    }

    public void PrintPersons()
    {
        var personsWithRelationships = GetPersonsWithRelationships();
        Console.WriteLine("+----------------+--------------------------+");
        Console.WriteLine("|      Name      |       Relationships      |");
        Console.WriteLine("+----------------+--------------------------+");

        foreach (var (person, relationships) in personsWithRelationships)
        {
            Console.WriteLine($"| {person.Name,-14} | {string.Join(", ", relationships)}");
        }

        Console.WriteLine("+----------------+-----+--------------------------+");
    }

    public void Dispose()
    {
        _driver?.Dispose();
    }
}