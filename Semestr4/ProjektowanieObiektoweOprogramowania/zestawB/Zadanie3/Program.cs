using System;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Configuration;

public interface IMyService
{
    void DoWork();
}

public class MyService : IMyService
{
    public void DoWork()
    {
        Console.WriteLine("MyService is working.");
    }
}

public abstract class MyBaseService
{
    public abstract void DoWork();
}

public class MyDerivedService : MyBaseService
{
    public override void DoWork()
    {
        Console.WriteLine("MyDerivedService is working.");
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        // Konfiguracja serwisów
        var services = new ServiceCollection();

        // Rejestracja typu
        services.AddTransient<MyService>();

        // Rejestracja typu na interfejs
        services.AddTransient<IMyService, MyService>();

        // Rejestracja typu na klasę abstrakcyjną
        services.AddTransient<MyBaseService, MyDerivedService>();

        // Rejestracja funkcji fabrykującej
        services.AddTransient<IMyService>(provider => new MyService());

        // Rejestracja instancji
        var myServiceInstance = new MyService();
        services.AddSingleton<IMyService>(myServiceInstance);

        // Zarządzanie czasem życia - Transient
        services.AddTransient<IMyService, MyService>();

        // Zarządzanie czasem życia - Singleton
        services.AddSingleton<MyService>();

        // Budowanie providera
        var provider = services.BuildServiceProvider();

        // Uzyskanie instancji wskazanego typu
        var myService = provider.GetService<MyService>();
        myService.DoWork();

        // Uzyskanie instancji implementującej wskazany interfejs
        var myServiceFromInterface = provider.GetService<IMyService>();
        myServiceFromInterface.DoWork();

        // Uzyskanie instancji implementującej klasę abstrakcyjną
        var myServiceFromAbstractClass = provider.GetService<MyBaseService>();
        myServiceFromAbstractClass.DoWork();

        // Zarządzanie czasem życia - Transient
        var transientService1 = provider.GetService<IMyService>();
        var transientService2 = provider.GetService<IMyService>();
        Console.WriteLine($"Transient services are different: {transientService1 != transientService2}");

        // Zarządzanie czasem życia - Singleton
        var singletonService1 = provider.GetService<MyService>();
        var singletonService2 = provider.GetService<MyService>();
        Console.WriteLine($"Singleton services are the same: {singletonService1 == singletonService2}");

        // JSON

        var configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("appsettings.json")
            .Build();

        var services2 = new ServiceCollection();

        // Pobieranie konfiguracji serwisów
        var serviceConfig2 = configuration.GetSection("Services");

        // Rejestracja serwisów na podstawie konfiguracji
        var myServiceType2 = Type.GetType(serviceConfig2["MyService"]);
        var myDerivedServiceType2 = Type.GetType(serviceConfig2["MyDerivedService"]);

        services2.AddTransient(typeof(IMyService), myServiceType2);
        services2.AddTransient(typeof(MyBaseService), myDerivedServiceType2);

        // Budowanie providera
        var provider2 = services2.BuildServiceProvider();

        // Uzyskanie instancji implementującej wskazany interfejs
        var myServiceFromInterface2 = provider2.GetService<IMyService>();
        myServiceFromInterface2.DoWork();

        // Uzyskanie instancji implementującej klasę abstrakcyjną
        var myServiceFromAbstractClass2 = provider2.GetService<MyBaseService>();
        myServiceFromAbstractClass2.DoWork();


    }
}
