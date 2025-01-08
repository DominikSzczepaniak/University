using eShop.Application;
using eShop.Domain.Entities;
using eShop.Domain.Entities.Repositories;
using NHibernate;
using Presentation.ConsoleApp;

public class Program
{
    public static void Main(string[] args)
        {
            ISession session = CreateSession();
            var productRepository = new NHibernateRepository<Product>(session);
            var productService = new ProductApplicationService(productRepository);

            while (true)
            {
                Console.Clear();
                Console.WriteLine("=== eShop Product Management ===");
                Console.WriteLine("1. View All Products");
                Console.WriteLine("2. View Product Details");
                Console.WriteLine("3. Add Product");
                Console.WriteLine("4. Update Product");
                Console.WriteLine("5. Delete Product");
                Console.WriteLine("6. Exit");
                Console.Write("Select an option: ");
                var choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        ViewAllProducts(productService);
                        break;
                    case "2":
                        ViewProductDetails(productService);
                        break;
                    case "3":
                        AddProduct(productService);
                        break;
                    case "4":
                        UpdateProduct(productService);
                        break;
                    case "5":
                        DeleteProduct(productService);
                        break;
                    case "6":
                        return;
                    default:
                        Console.WriteLine("Invalid choice. Press Enter to try again...");
                        Console.ReadLine();
                        break;
                }
            }
        }

    static void ViewAllProducts(IProductApplicationService productService)
    {
        var viewService = new ProductViewService(productService);

        Console.Clear();
        Console.Write("Enter search keyword (or leave blank): ");
        string search = Console.ReadLine();

        Console.Write("Enter sort field (Name/Price): ");
        string sortBy = Console.ReadLine();

        Console.Write("Sort descending? (y/n): ");
        bool descending = Console.ReadLine().ToLower() == "y";

        Console.Write("Enter page number: ");
        int.TryParse(Console.ReadLine(), out int pageNumber);
        pageNumber = pageNumber > 0 ? pageNumber : 1;

        Console.Write("Enter page size: ");
        int.TryParse(Console.ReadLine(), out int pageSize);
        pageSize = pageSize > 0 ? pageSize : 10;

        var productView = viewService.GetProductsView(search, sortBy, descending, pageNumber, pageSize);

        Console.WriteLine($"\n=== Products (Page {productView.PageNumber} of {productView.TotalPages}) ===");
        foreach (var product in productView.Products)
        {
            Console.WriteLine($"ID: {product.Id}, Name: {product.Name}, Price: {product.Price:C}");
        }

        Console.WriteLine("\nPress Enter to return to the main menu...");
        Console.ReadLine();
    }



        static void ViewProductDetails(IProductApplicationService productService)
        {
            Console.Clear();
            Console.Write("Enter Product ID: ");
            if (Guid.TryParse(Console.ReadLine(), out var productId))
            {
                var product = productService.GetProductById(productId);
                if (product != null)
                {
                    Console.WriteLine($"ID: {product.Id}");
                    Console.WriteLine($"Name: {product.Name}");
                    Console.WriteLine($"Description: {product.Description}");
                    Console.WriteLine($"Price: {product.Price:C}");
                }
                else
                {
                    Console.WriteLine("Product not found.");
                }
            }
            else
            {
                Console.WriteLine("Invalid ID format.");
            }

            Console.WriteLine("Press Enter to return to the main menu...");
            Console.ReadLine();
        }

        static void AddProduct(IProductApplicationService productService)
        {
            Console.Clear();
            Console.Write("Enter Product Name: ");
            var name = Console.ReadLine();
            Console.Write("Enter Product Description: ");
            var description = Console.ReadLine();
            Console.Write("Enter Product Price: ");
            if (decimal.TryParse(Console.ReadLine(), out var price))
            {
                productService.CreateProduct(name, description, price);
                Console.WriteLine("Product added successfully.");
            }
            else
            {
                Console.WriteLine("Invalid price format.");
            }

            Console.WriteLine("Press Enter to return to the main menu...");
            Console.ReadLine();
        }

        static void UpdateProduct(IProductApplicationService productService)
        {
            Console.Clear();
            Console.Write("Enter Product ID: ");
            if (Guid.TryParse(Console.ReadLine(), out var productId))
            {
                Console.Write("Enter New Product Name: ");
                var name = Console.ReadLine();
                Console.Write("Enter New Product Description: ");
                var description = Console.ReadLine();
                Console.Write("Enter New Product Price: ");
                if (decimal.TryParse(Console.ReadLine(), out var price))
                {
                    try
                    {
                        productService.UpdateProduct(productId, name, description, price);
                        Console.WriteLine("Product updated successfully.");
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"Error: {ex.Message}");
                    }
                }
                else
                {
                    Console.WriteLine("Invalid price format.");
                }
            }
            else
            {
                Console.WriteLine("Invalid ID format.");
            }

            Console.WriteLine("Press Enter to return to the main menu...");
            Console.ReadLine();
        }

        static void DeleteProduct(IProductApplicationService productService)
        {
            Console.Clear();
            Console.Write("Enter Product ID: ");
            if (Guid.TryParse(Console.ReadLine(), out var productId))
            {
                try
                {
                    productService.DeleteProduct(productId);
                    Console.WriteLine("Product deleted successfully.");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error: {ex.Message}");
                }
            }
            else
            {
                Console.WriteLine("Invalid ID format.");
            }

            Console.WriteLine("Press Enter to return to the main menu...");
            Console.ReadLine();
        }

        static ISession CreateSession()
        {
            // Replace with actual NHibernate session factory setup.
            throw new NotImplementedException("Setup your NHibernate session here.");
        }

}