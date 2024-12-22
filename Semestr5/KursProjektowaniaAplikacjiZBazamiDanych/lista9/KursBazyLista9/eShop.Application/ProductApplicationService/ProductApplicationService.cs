using eShop.Domain.Entities;
using eShop.Domain.Entities.Repositories;
using System;
using System.Collections.Generic;
using eShop.Domain.ValueObjects;

namespace eShop.Application
{
    public class ProductApplicationService(IBaseRepository<Product> productRepository) : IProductApplicationService
    {
        public IEnumerable<Product> GetAllProducts()
        {
            return productRepository.FindAll();
        }

        public Product GetProductById(Guid id)
        {
            return productRepository.Find(id);
        }

        public void CreateProduct(string name, string description, decimal price)
        {
            var product = new Product(name, description, price);
            productRepository.Add(product);
        }

        public void UpdateProduct(Guid id, string name, string description, decimal price)
        {
            var product = productRepository.Find(id);
            if (product == null)
            {
                throw new ArgumentException("Product not found.");
            }
            product.UpdateDetails(name, description, price);
            productRepository.Update(product);
        }

        public void DeleteProduct(Guid id)
        {
            productRepository.Delete(id);
        }
    }
}