using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

class Program
{
    static void Main(string[] args)
    {
        using (var context = new MyDbContext())
        {
            var parent = new Parent { imie = "Jan", nazwisko = "Kowalski" };
            context.Parents.Add(parent);
            context.SaveChanges();

            var child = new Child { imie = "Anna", nazwisko = "Kowalska", id_parent = parent.id };
            context.Children.Add(child);
            context.SaveChanges();

            var parentsWithChildren = context.Parents.Include(p => p.Children).ToList();
            foreach (var p in parentsWithChildren)
            {
                Console.WriteLine($"{p.imie} {p.nazwisko}");
                foreach (var c in p.Children)
                {
                    Console.WriteLine($"  - {c.imie} {c.nazwisko}");
                }
            }

            var firstParent = context.Parents.First();
            firstParent.imie = "Janusz";
            context.SaveChanges();

            var firstChild = context.Children.First();
            context.Children.Remove(firstChild);
            context.SaveChanges();
        }
    }
}

public class Parent
{
    public int id { get; set; }
    public string imie { get; set; }
    public string nazwisko { get; set; }
    public ICollection<Child> Children { get; set; }
}

public class Child
{
    public int id { get; set; }
    public string imie { get; set; }
    public string nazwisko { get; set; }
    public int id_parent { get; set; }
    public Parent Parent { get; set; }
}

public class MyDbContext : DbContext
{
    public DbSet<Parent> Parents { get; set; }
    public DbSet<Child> Children { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseNpgsql("Host=localhost;Port=5432;Database=poozestawC;Username=poo;Password=poo");
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Parent>(entity =>
        {
            entity.ToTable("parent");
            entity.HasKey(p => p.id);
        });

        modelBuilder.Entity<Child>(entity =>
        {
            entity.ToTable("child");
            entity.HasKey(c => c.id);

            entity.HasOne(c => c.Parent)
                .WithMany(p => p.Children)
                .HasForeignKey(c => c.id_parent);
        });
    }
}


// Polityka czasu życia sesji:
// Aplikacja desktop
// Długi czas życia sesji, sesja dostępu do danych (np. połączenie z bazą danych) często jest inicjowana na początku działania aplikacji i utrzymywana przez cały czas jej działania.
// Jest to praktyczne, ponieważ aplikacje desktopowe zazwyczaj działają na jednym urządzeniu i nie mają ograniczeń wynikających z architektury sieciowej.
// Aplikacja webowa
//Krótki czas życia sesji: W aplikacjach webowych sesje dostępu do danych powinny mieć krótszy czas życia. Typowo są inicjowane na początku obsługi każdego żądania HTTP
//i niszczone po zakończeniu obsługi tego żądania. Pozwala to na lepszą skalowalność i zarządzanie zasobami w środowiskach wieloużytkownikowych.

// Inicjowanie sesji:
//Desktop
// Sesja może być inicjowana podczas uruchamiania aplikacji, zazwyczaj w metodzie głównej (main) lub w momencie, gdy użytkownik loguje się do aplikacji.
//Web
//Sesja dostępu do danych jest inicjowana na początku każdego żądania. W kontekście frameworków webowych, takich jak ASP.NET, sesja może być inicjowana w metodach pośredniczących (middleware) lub na początku kontrolera.

// Niszczenie sesji:
//Desktop
// Sesja jest zazwyczaj niszczona podczas zamykania aplikacji lub gdy użytkownik się wylogowuje. Ważne jest, aby zapewnić właściwe zwalnianie zasobów, takie jak zamykanie połączeń z bazą danych i zwalnianie pamięci.
//Web
// Sesja powinna być niszczona po zakończeniu obsługi żądania. Frameworki webowe często automatycznie zarządzają cyklem życia sesji, zamykając połączenia z bazą danych po przetworzeniu żądania.



// Kluczowe zasady zarządzania sesjami dostępu do danych
// Zasada minimalnego czasu życia:
// Staraj się utrzymywać sesje (np. połączenia z bazą danych) otwarte tylko tak długo, jak to jest konieczne. Pozwala to na lepsze zarządzanie zasobami, zwłaszcza w aplikacjach
// webowych, gdzie zasoby mogą być szybko wyczerpane przez wielu jednoczesnych użytkowników.

// Zasada jednego żądania:
// W aplikacjach webowych każde żądanie HTTP powinno być obsługiwane w ramach swojej własnej, niezależnej sesji dostępu do danych. Zapobiega to problemom związanym z wielowątkowością i konkurencją.

// Zwalnianie zasobów:
// Bez względu na typ aplikacji, zawsze należy dbać o poprawne zwalnianie zasobów po zakończeniu ich użycia. Dotyczy to zamykania połączeń z bazą danych, zwalniania pamięci i innych zasobów systemowych.

// Obsługa wyjątków:
// Sesje powinny być zarządzane w sposób bezpieczny, z odpowiednią obsługą wyjątków, aby uniknąć przecieków zasobów. W C# można do tego wykorzystać konstrukcję using lub odpowiednie bloki try-finally.
// Przestrzeganie tych zasad pomoże w zapewnieniu efektywnego i skalowalnego zarządzania sesjami dostępu do danych zarówno w aplikacjach desktopowych, jak i webowych.