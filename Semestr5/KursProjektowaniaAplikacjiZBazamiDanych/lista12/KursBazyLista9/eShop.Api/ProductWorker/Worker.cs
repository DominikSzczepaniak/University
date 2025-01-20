using Azure.Messaging.ServiceBus;
using eShop.Application;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System.Text.Json;
using System.Threading;
using System.Threading.Tasks;
using eShop.Api.Controllers;
public class Worker : BackgroundService
{
    private readonly ILogger<Worker> _logger;
    private readonly IProductApplicationService _productService;
    private readonly string serviceBusConnectionString = "<Your-Service-Bus-Connection-String>";
    private readonly string queueName = "product-queue";
    private ServiceBusProcessor _processor;

    public Worker(ILogger<Worker> logger, IProductApplicationService productService)
    {
        _logger = logger;
        _productService = productService;

        var client = new ServiceBusClient(serviceBusConnectionString);
        _processor = client.CreateProcessor(queueName, new ServiceBusProcessorOptions());
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        _processor.ProcessMessageAsync += async args =>
        {
            var body = args.Message.Body.ToString();
            var productRequest = JsonSerializer.Deserialize<CreateProductRequest>(body);

            _logger.LogInformation($"Processing product: {productRequest.Name}");

            _productService.CreateProduct(productRequest.Name, productRequest.Description, productRequest.Price);

            await args.CompleteMessageAsync(args.Message);
        };

        _processor.ProcessErrorAsync += args =>
        {
            _logger.LogError($"Message handler encountered an error: {args.Exception}");
            return Task.CompletedTask;
        };

        await _processor.StartProcessingAsync();
        _logger.LogInformation("Worker started processing messages.");
    }

    public override async Task StopAsync(CancellationToken stoppingToken)
    {
        await _processor.StopProcessingAsync();
        await base.StopAsync(stoppingToken);
    }
}