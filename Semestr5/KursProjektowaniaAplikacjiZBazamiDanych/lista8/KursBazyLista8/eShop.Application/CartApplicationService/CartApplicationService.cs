using eShop.Domain.Entities;
using eShop.Domain.Entities.Repositories;
using eShop.Domain.ValueObjects;
using System;
using System.Collections.Generic;
using System.Linq;

namespace eShop.Application.CartApplicationService
{
    public class CartApplicationService(
        IBaseRepository<Cart> cartRepository,
        IBaseRepository<Product> productRepository)
        : ICartApplicationService
    {
        public Cart GetCartById(Guid cartId)
        {
            return cartRepository.GetById(cartId);
        }

        public void AddProductToCart(Guid cartId, Guid productId, int quantity)
        {
            var cart = cartRepository.GetById(cartId);
            var product = productRepository.GetById(productId);

            if (product == null)
            {
                throw new ArgumentException("Product not found.");
            }

            var cartItem = new CartItem(productId, quantity);
            cart.AddItem(cartItem);
            cartRepository.Update(cart);
        }

        public void RemoveProductFromCart(Guid cartId, Guid productId)
        {
            var cart = cartRepository.GetById(cartId);
            cart.RemoveItem(productId);
            cartRepository.Update(cart);
        }

        public void ClearCart(Guid cartId)
        {
            var cart = cartRepository.GetById(cartId);
            cart.Items.Clear();
            cartRepository.Update(cart);
        }

        public void CheckoutCart(Guid cartId)
        {
            var cart = cartRepository.GetById(cartId);
            cart.Checkout();
            cartRepository.Update(cart);
        }

        public IEnumerable<CartItem> GetCartItems(Guid cartId)
        {
            var cart = cartRepository.GetById(cartId);
            return cart.Items;
        }
    }
}