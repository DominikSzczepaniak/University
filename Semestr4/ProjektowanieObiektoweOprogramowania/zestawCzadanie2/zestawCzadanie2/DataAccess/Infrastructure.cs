using SimpleTaskManager.Domain;
using System.Collections.Generic;
using System.Linq;
using Microsoft.EntityFrameworkCore;
using SimpleTaskManager.Application;

namespace SimpleTaskManager.Infrastructure
{
    public class ParentRepository : IParentRepository
    {
        private readonly MyDbContext _context;

        public ParentRepository(MyDbContext context)
        {
            _context = context;
        }

        public void Add(Parent parent)
        {
            _context.Parents.Add(parent);
            _context.SaveChanges();
        }

        public void Update(Parent parent)
        {
            _context.Parents.Update(parent);
            _context.SaveChanges();
        }

        public void Delete(Parent parent)
        {
            _context.Parents.Remove(parent);
            _context.SaveChanges();
        }

        public Parent GetById(int id)
        {
            return _context.Parents.Find(id);
        }

        public IEnumerable<Parent> GetAllWithChildren()
        {
            return _context.Parents.ToList();
        }
    }

    public class ChildRepository : IChildRepository
    {
        private readonly MyDbContext _context;

        public ChildRepository(MyDbContext context)
        {
            _context = context;
        }

        public void Add(Child child)
        {
            _context.Children.Add(child);
            _context.SaveChanges();
        }
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
                entity.ToTable("parent");  // Ustaw nazwę tabeli na "parent"
                entity.HasKey(p => p.id);
            });

            modelBuilder.Entity<Child>(entity =>
            {
                entity.ToTable("child");  // Ustaw nazwę tabeli na "child"
                entity.HasKey(c => c.id);

                entity.HasOne(c => c.Parent)
                    .WithMany(p => p.Children)
                    .HasForeignKey(c => c.id_parent);
            });
        }
    }

}