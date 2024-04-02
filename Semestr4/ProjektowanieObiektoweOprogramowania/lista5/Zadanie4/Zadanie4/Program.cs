using System;
using System.Collections.Generic;

// Implementacja mostu dla pierwszego stopnia swobody
public interface IDataLoader
{
    List<Person> LoadPersons();
}

// Konkretne implementacje mostu dla wczytywania danych z różnych źródeł
public class XmlDataLoader : IDataLoader
{
    public List<Person> LoadPersons()
    {
        // Implementacja wczytywania danych z XML
        Console.WriteLine("Loading persons from XML...");
        return new List<Person>();
    }
}

public class DatabaseDataLoader : IDataLoader
{
    public List<Person> LoadPersons()
    {
        // Implementacja wczytywania danych z bazy danych
        Console.WriteLine("Loading persons from database...");
        return new List<Person>();
    }
}

// Implementacja mostu dla drugiego stopnia swobody
public interface INotifier
{
    void NotifyPersons(List<Person> persons);
}

// Konkretne implementacje mostu dla powiadamiania pracowników różnymi sposobami
public class EmailNotifier : INotifier
{
    public void NotifyPersons(List<Person> persons)
    {
        // Implementacja powiadamiania przez e-mail
        Console.WriteLine("Notifying persons via email...");
    }
}

public class SmsNotifier : INotifier
{
    public void NotifyPersons(List<Person> persons)
    {
        // Implementacja powiadamiania przez SMS
        Console.WriteLine("Notifying persons via SMS...");
    }
}

// Abstrakcyjna klasa rejestru pracowników wykorzystująca most
public abstract class PersonRegistry
{
    protected IDataLoader dataLoader;
    protected INotifier notifier;

    public PersonRegistry(IDataLoader dataLoader, INotifier notifier)
    {
        this.dataLoader = dataLoader;
        this.notifier = notifier;
    }

    public abstract void ProcessRegistry();
}

// Konkretne implementacje klasy rejestru pracowników z różnymi sposobami wczytywania danych i powiadamiania pracowników
public class XmlEmailPersonRegistry : PersonRegistry
{
    public XmlEmailPersonRegistry(IDataLoader dataLoader, INotifier notifier) : base(dataLoader, notifier)
    {
    }

    public override void ProcessRegistry()
    {
        var persons = dataLoader.LoadPersons();
        notifier.NotifyPersons(persons);
    }
}

public class DatabaseSmsPersonRegistry : PersonRegistry
{
    public DatabaseSmsPersonRegistry(IDataLoader dataLoader, INotifier notifier) : base(dataLoader, notifier)
    {
    }

    public override void ProcessRegistry()
    {
        var persons = dataLoader.LoadPersons();
        notifier.NotifyPersons(persons);
    }
}

// Klasa reprezentująca osobę
public class Person
{
    // Dane osoby
}

class Program
{
    static void Main(string[] args)
    {
        // Przykładowe użycie mostu
        IDataLoader xmlDataLoader = new XmlDataLoader();
        INotifier emailNotifier = new EmailNotifier();
        PersonRegistry xmlEmailPersonRegistry = new XmlEmailPersonRegistry(xmlDataLoader, emailNotifier);
        xmlEmailPersonRegistry.ProcessRegistry();

        IDataLoader databaseDataLoader = new DatabaseDataLoader();
        INotifier smsNotifier = new SmsNotifier();
        PersonRegistry databaseSmsPersonRegistry = new DatabaseSmsPersonRegistry(databaseDataLoader, smsNotifier);
        databaseSmsPersonRegistry.ProcessRegistry();
    }
}
