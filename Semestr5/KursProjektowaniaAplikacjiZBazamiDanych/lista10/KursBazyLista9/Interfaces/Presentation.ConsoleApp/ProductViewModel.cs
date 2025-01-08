using eShop.Application;

namespace Presentation.ConsoleApp.Models;

public class ProductViewModel
{
    public IEnumerable<ProductDto> Products { get; set; } = new List<ProductDto>();
    public string SearchKeyword { get; set; }
    public string SortBy { get; set; } = "Name";
    public bool Descending { get; set; }
    public int PageNumber { get; set; } = 1;
    public int PageSize { get; set; } = 10;
    public int TotalPages { get; set; }
}