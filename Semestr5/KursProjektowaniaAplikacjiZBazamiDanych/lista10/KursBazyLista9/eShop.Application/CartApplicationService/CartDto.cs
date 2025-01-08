namespace eShop.Application.CartApplicationService;

public class CartDto
{
    public Guid Id { get; set; }
    public bool IsCheckedOut { get; set; }
    public List<CartItemDto> Items { get; set; } = new();
}