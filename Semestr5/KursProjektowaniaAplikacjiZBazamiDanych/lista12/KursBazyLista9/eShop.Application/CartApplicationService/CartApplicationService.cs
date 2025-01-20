using eShop.Domain.Entities;
using eShop.Domain.Entities.Repositories;
using eShop.Domain.ValueObjects;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;

namespace eShop.Application.CartApplicationService;

public class CartApplicationService : ICartApplicationService
{
    private readonly IBaseRepository<Cart> cartRepository;

    public CartApplicationService(IBaseRepository<Cart> cartRepository)
    {
        this.cartRepository = cartRepository;
    }

    public CartDto GetCartById(Guid cartId) => MapToDto(cartRepository.Find(cartId));

    public IEnumerable<CartDto> GetAllCarts(
        string search = null,
        string sortBy = "Id",
        bool descending = false,
        int pageNumber = 1,
        int pageSize = 10)
    {
        Expression<Func<Cart, bool>> filter = null;

        if (!string.IsNullOrEmpty(search))
        {
            filter = c => c.Id.ToString().Contains(search) ||
                          c.Items.Any(i => i.ProductId.ToString().Contains(search));
        }

        Func<IQueryable<Cart>, IOrderedQueryable<Cart>> orderBy = query =>
            sortBy switch
            {
                "Id" => descending ? query.OrderByDescending(c => c.Id) : query.OrderBy(c => c.Id),
                "IsCheckedOut" => descending ? query.OrderByDescending(c => c.IsCheckedOut) : query.OrderBy(c => c.IsCheckedOut),
                _ => query.OrderBy(c => c.Id)
            };

        return cartRepository.FindAll(filter, orderBy, pageNumber, pageSize).Select(MapToDto);
    }

    public void AddProductToCart(Guid cartId, Guid productId, int quantity)
    {
        var cart = cartRepository.Find(cartId);
        cart.AddItem(new CartItem(productId, quantity));
        cartRepository.Update(cart);
    }

    public void RemoveProductFromCart(Guid cartId, Guid productId)
    {
        var cart = cartRepository.Find(cartId);
        cart.RemoveItem(productId);
        cartRepository.Update(cart);
    }

    public void ClearCart(Guid cartId)
    {
        var cart = cartRepository.Find(cartId);
        cart.Items.Clear();
        cartRepository.Update(cart);
    }

    public void CheckoutCart(Guid cartId)
    {
        var cart = cartRepository.Find(cartId);
        cart.Checkout();
        cartRepository.Update(cart);
    }

    public IEnumerable<CartItem> GetCartItems(Guid cartId)
    {
        var cart = cartRepository.Find(cartId);
        return cart.Items;
    }

    private static CartDto MapToDto(Cart cart) => new()
    {
        Id = cart.Id,
        IsCheckedOut = cart.IsCheckedOut,
        Items = cart.Items.Select(MapToDtoItem).ToList(),
    };

    private static CartItemDto MapToDtoItem(CartItem cartItem) => new()
    {
        ProductId = cartItem.ProductId,
        Quantity = cartItem.Quantity,
    };
}