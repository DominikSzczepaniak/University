using eShop.Domain.ValueObjects;

namespace eShop.Domain.Entities;

public class Cart : IEntity
{
    public Guid Id { get; private set; } = Guid.NewGuid();
    public List<CartItem> Items { get; private set; } = new();
    public bool IsCheckedOut { get; private set; } = false;
    
    public void AddItem(CartItem item)
    {
        if (IsCheckedOut)
            throw new InvalidOperationException("Cannot add items to a checked-out cart.");
    
        var existingItem = Items.FirstOrDefault(i => i.ProductId == item.ProductId);
        if (existingItem != null)
        {
            existingItem.UpdateQuantity(existingItem.Quantity + item.Quantity);
        }
        else
        {
            Items.Add(item);
        }
    }

    public void RemoveItem(Guid productId)
    {
        if (IsCheckedOut)
            throw new InvalidOperationException("Cannot remove items from a checked-out cart.");
    
        Items.RemoveAll(item => item.ProductId == productId);
    }
    
    public void Checkout()
    {
        if (IsCheckedOut)
            throw new InvalidOperationException("Cart is already checked out.");
    
        IsCheckedOut = true;
    }
}