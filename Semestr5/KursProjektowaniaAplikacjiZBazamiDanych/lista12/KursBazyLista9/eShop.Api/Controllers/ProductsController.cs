using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Text.Json;
using Azure.Messaging.ServiceBus;
using eShop.Application;
using eShop.Domain.Entities;
namespace eShop.Api.Controllers;

[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    private readonly IProductApplicationService _productService;
    private readonly string serviceBusConnectionString = "<Your-Service-Bus-Connection-String>";
    private readonly string queueName = "product-queue";


    public ProductsController(IProductApplicationService productService)
    {
        _productService = productService;
    }

    [HttpGet]
    public IActionResult GetAllProducts(
        [FromQuery] string search = null,
        [FromQuery] string sortBy = "Name",
        [FromQuery] bool descending = false,
        [FromQuery] int pageNumber = 1,
        [FromQuery] int pageSize = 10)
    {
        var products = _productService.GetAllProducts(search, sortBy, descending, pageNumber, pageSize);
        return Ok(products);
    }

    [HttpGet("{id}")]
    public IActionResult GetProductById(Guid id)
    {
        var product = _productService.GetProductById(id);
        if (product == null)
        {
            return NotFound();
        }

        return Ok(product);
    }

    [HttpPost]
    public async Task<IActionResult> CreateProduct([FromBody] CreateProductRequest request)
    {
        if (!ModelState.IsValid)
        {
            return BadRequest(ModelState);
        }

        var productMessage = JsonSerializer.Serialize(request);

        await using var client = new ServiceBusClient(serviceBusConnectionString);
        var sender = client.CreateSender(queueName);

        try
        {
            var message = new ServiceBusMessage(productMessage);
            await sender.SendMessageAsync(message);
            return Accepted(); // Return 202 Accepted
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"Error sending message: {ex.Message}");
        }
    }

    [HttpPut("{id}")]
    public IActionResult UpdateProduct(Guid id, [FromBody] UpdateProductRequest request)
    {
        if (!ModelState.IsValid)
        {
            return BadRequest(ModelState);
        }

        try
        {
            _productService.UpdateProduct(id, request.Name, request.Description, request.Price);
            return NoContent();
        }
        catch (ArgumentException ex)
        {
            return NotFound(ex.Message);
        }
    }

    [HttpDelete("{id}")]
    public IActionResult DeleteProduct(Guid id)
    {
        try
        {
            _productService.DeleteProduct(id);
            return NoContent();
        }
        catch (ArgumentException ex)
        {
            return NotFound(ex.Message);
        }
    }
}

public class CreateProductRequest
{
    public string Name { get; set; }
    public string Description { get; set; }
    public decimal Price { get; set; }
}

public class UpdateProductRequest
{
    public string Name { get; set; }
    public string Description { get; set; }
    public decimal Price { get; set; }
}

