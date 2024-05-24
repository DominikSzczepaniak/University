using System;

class Program
{
    static void Main(string[] args)
    {
        var archiveHandler = new ArchiveHandler();
        var invalidMessageHandler = new InvalidMessageHandler();
        var orderHandler = new OrderHandler();
        var complaintHandler = new ComplaintHandler();
        var praiseHandler = new PraiseHandler();
        var classifier = new ClassifierHandler();

        classifier.SetNext(praiseHandler)
                  .SetNext(complaintHandler)
                  .SetNext(orderHandler)
                  .SetNext(invalidMessageHandler)
                  .SetNext(archiveHandler);

        var requests = new[]
        {
            new Request { Title = "Great Service!", Content = "Thank you for the wonderful service." },
            new Request { Title = "Complaint", Content = "My order was late and the product was damaged." },
            new Request { Title = "Order", Content = "I would like to order 20 units of product XYZ." },
            new Request { Title = "Spam", Content = "" }
        };

        foreach (var request in requests)
        {
            classifier.Handle(request);
            Console.WriteLine();
        }
    }
}

class Request
{
    public string Title { get; set; }
    public string Content { get; set; }
    public string MessageType { get; set; }
}

abstract class Handler
{
    protected Handler next;

    public Handler SetNext(Handler nextHandler)
    {
        next = nextHandler;
        return nextHandler;
    }

    public virtual void Handle(Request request)
    {
        next?.Handle(request);
    }
}

class ClassifierHandler : Handler
{
    public override void Handle(Request request)
    {
        if (string.IsNullOrEmpty(request.Content))
        {
            request.MessageType = "Invalid";
        }
        else if (request.Title.ToLower().Contains("thank"))
        {
            request.MessageType = "Praise";
        }
        else if (request.Title.ToLower().Contains("complaint"))
        {
            request.MessageType = "Complaint";
        }
        else if (request.Title.ToLower().Contains("order"))
        {
            request.MessageType = "Order";
        }
        else
        {
            request.MessageType = "Other";
        }

        base.Handle(request);
    }
}

class PraiseHandler : Handler
{
    public override void Handle(Request request)
    {
        if (request.MessageType == "Praise")
        {
            Console.WriteLine($"Handling Praise: {request.Content}");
        }
        base.Handle(request);
    }
}

class ComplaintHandler : Handler
{
    public override void Handle(Request request)
    {
        if (request.MessageType == "Complaint")
        {
            Console.WriteLine($"Handling Complaint: {request.Content}");
        }
        base.Handle(request);
    }
}

class OrderHandler : Handler
{
    public override void Handle(Request request)
    {
        if (request.MessageType == "Order")
        {
            Console.WriteLine($"Handling Order: {request.Content}");
        }
        base.Handle(request);
    }
}

class InvalidMessageHandler : Handler
{
    public override void Handle(Request request)
    {
        if (request.MessageType == "Invalid")
        {
            Console.WriteLine($"Handling Invalid Message: Please check the content.");
        }
        base.Handle(request);
    }
}

class ArchiveHandler : Handler
{
    public override void Handle(Request request)
    {
        Console.WriteLine($"Archiving Message: {request.Title}");
    }
}
