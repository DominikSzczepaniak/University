using Zadanie4i5;

class Program
{
    private const string Uri = "neo4j+s://lolz.databases.neo4j.io";
    private const string User = "neo4j";
    private const string Password = "not for you to know";

    public static void Main()
    {
        // Zad4();
        Zad5();
    }

    public static void Zad4()
    {
        var zadanie4 = new Zadanie4(Uri, User, Password);
        zadanie4.PrintPersons();
    }

    public static void Zad5()
    {
        var zadanie5 = new Zadanie5(Uri, User, Password);
        zadanie5.CreatePerson("John Doe");
        zadanie5.CreatePerson("Jane Doe");

        zadanie5.PrintPersons();

        zadanie5.UpdatePerson("John Doe", "John Notdoe");
        zadanie5.PrintPersons();

        zadanie5.DeletePerson("Jane Doe");
        zadanie5.PrintPersons();
    }
}
