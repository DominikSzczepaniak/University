using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using eShop.Domain.Entities;
using eShop.Domain.Entities.Repositories;

namespace eShop.Application
{
    public class ProductApplicationService : IProductApplicationService
    {
        private readonly IBaseRepository<Product> productRepository;

        public ProductApplicationService(IBaseRepository<Product> productRepository)
        {
            this.productRepository = productRepository;
        }

        public IEnumerable<ProductDto> GetAllProducts()
        {
            return productRepository.FindAll().Select(MapToDto);
        }

        public IEnumerable<ProductDto> GetAllProducts(
            string search = null,
            string sortBy = "Name",
            bool descending = false,
            int pageNumber = 1,
            int pageSize = 10)
        {
            Expression<Func<Product, bool>> filter = null;
            if (!string.IsNullOrEmpty(search))
            {
                filter = p => p.Name.Contains(search) || p.Description.Contains(search);
            }

            Func<IQueryable<Product>, IOrderedQueryable<Product>> orderBy = query =>
                sortBy switch
                {
                    "Name" => descending ? query.OrderByDescending(p => p.Name) : query.OrderBy(p => p.Name),
                    "Price" => descending ? query.OrderByDescending(p => p.Price) : query.OrderBy(p => p.Price),
                    _ => query.OrderBy(p => p.Name)
                };

            var products = productRepository.FindAll(filter, orderBy, pageNumber, pageSize);
            return products.Select(MapToDto);
        }

        public ProductDto GetProductById(Guid id)
        {
            var product = productRepository.Find(id);
            return product == null ? null : MapToDto(product);
        }

        public Product CreateProduct(string name, string description, decimal price)
        {
            var product = new Product(name, description, price);
            productRepository.Add(product);
            return product;
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

        private static ProductDto MapToDto(Product product) => new()
        {
            Id = product.Id,
            Name = product.Name,
            Description = product.Description,
            Price = product.Price
        };
    }
}