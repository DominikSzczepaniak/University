namespace eShop.Domain.ValueObjects;

public class CartItem(Guid productId, int quantity)
{
    public Guid ProductId { get; private set; } = productId;
    public int Quantity { get; private set; } = quantity;

    public void UpdateQuantity(int newQuantity) => Quantity = newQuantity;
}