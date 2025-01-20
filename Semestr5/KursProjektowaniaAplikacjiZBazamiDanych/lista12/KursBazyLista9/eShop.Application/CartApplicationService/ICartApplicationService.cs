using eShop.Domain.Entities;
using eShop.Domain.ValueObjects;

namespace eShop.Application.CartApplicationService;

public interface ICartApplicationService
{
    CartDto GetCartById(Guid cartId);
    IEnumerable<CartDto> GetAllCarts(
        string search = null,
        string sortBy = "Id",
        bool descending = false,
        int pageNumber = 1,
        int pageSize = 10);
    void AddProductToCart(Guid cartId, Guid productId, int quantity);
    void RemoveProductFromCart(Guid cartId, Guid productId);
    void ClearCart(Guid cartId);
    void CheckoutCart(Guid cartId);
    IEnumerable<CartItem> GetCartItems(Guid cartId);
}