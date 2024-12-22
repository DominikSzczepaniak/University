using eShop.Domain.Entities;

namespace eShop.Application;

public interface IProductApplicationService
{
    IEnumerable<Product> GetAllProducts();
    Product GetProductById(Guid id);
    void CreateProduct(string name, string description, decimal price);
    void UpdateProduct(Guid id, string name, string description, decimal price);
    void DeleteProduct(Guid id);
}
