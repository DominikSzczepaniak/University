using eShop.Domain.Entities;
using eShop.Domain.ValueObjects;

namespace eShop.Application.CartApplicationService;

public interface ICartApplicationService
{
    Cart GetCartById(Guid cartId);
    void AddProductToCart(Guid cartId, Guid productId, int quantity);
    void RemoveProductFromCart(Guid cartId, Guid productId);
    void ClearCart(Guid cartId);
    void CheckoutCart(Guid cartId);
    IEnumerable<CartItem> GetCartItems(Guid cartId);
}
