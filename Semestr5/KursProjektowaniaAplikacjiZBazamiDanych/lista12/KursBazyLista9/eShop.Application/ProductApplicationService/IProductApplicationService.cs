using System;
using System.Collections.Generic;
using eShop.Domain.Entities;

namespace eShop.Application
{
    public interface IProductApplicationService
    {
        IEnumerable<ProductDto> GetAllProducts();
        IEnumerable<ProductDto> GetAllProducts(
            string search = null,
            string sortBy = "Name",
            bool descending = false,
            int pageNumber = 1,
            int pageSize = 10);
        ProductDto GetProductById(Guid id);
        Product CreateProduct(string name, string description, decimal price);
        void UpdateProduct(Guid id, string name, string description, decimal price);
        void DeleteProduct(Guid id);
    }
}