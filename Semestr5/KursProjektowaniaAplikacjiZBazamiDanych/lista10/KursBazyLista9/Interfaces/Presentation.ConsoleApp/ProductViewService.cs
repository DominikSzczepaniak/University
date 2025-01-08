using eShop.Application;
using eShop.Application.UserApplicationService;
using Presentation.ConsoleApp.Models;

namespace Presentation.ConsoleApp;

public class ProductViewService
{
    private readonly IProductApplicationService _productService;

    public ProductViewService(IProductApplicationService productService)
    {
        _productService = productService;
    }

    public ProductViewModel GetProductsView(
        string search = null,
        string sortBy = "Name",
        bool descending = false,
        int pageNumber = 1,
        int pageSize = 10)
    {
        var products = _productService.GetAllProducts(search, sortBy, descending, pageNumber, pageSize).ToList();

        int totalProducts = products.Count;
        int totalPages = (int)Math.Ceiling((double)totalProducts / pageSize);

        return new ProductViewModel
        {
            Products = products,
            SearchKeyword = search,
            SortBy = sortBy,
            Descending = descending,
            PageNumber = pageNumber,
            PageSize = pageSize,
            TotalPages = totalPages
        };
    }
}