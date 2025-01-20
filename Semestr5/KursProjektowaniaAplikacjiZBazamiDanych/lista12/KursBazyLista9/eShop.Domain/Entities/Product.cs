using eShop.Domain.ValueObjects;

namespace eShop.Domain.Entities;

public class Product(string name, string description, decimal price) : IEntity
{
    public Guid Id { get; private set; }
    public string Name { get; private set; } = name;
    public string Description { get; private set; } = description;
    public decimal Price { get; private set; } = price;

    public void UpdateDetails(string name, string description, decimal price)
    {
        Name = name;
        Description = description;
        Price = price;
    }
}