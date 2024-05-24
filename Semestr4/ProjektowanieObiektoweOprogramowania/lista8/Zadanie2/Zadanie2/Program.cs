using System;
using System.IO;
using System.Net;
using System.Threading;
using System.Collections.Concurrent;

class Program
{
    static void Main()
    {
        var queue = new ConcurrentQueue<ICommand>();
        var receiver = new FileOperationReceiver();
        var invoker = new CommandInvoker(queue);

        invoker.StartProcessing();

        queue.Enqueue(new FtpDownloadCommand(receiver, "examplefile.txt"));
        queue.Enqueue(new HttpDownloadCommand(receiver, "http://example.com/file.txt"));
        queue.Enqueue(new CreateAndFillFileCommand(receiver, "newfile.txt", 1024));
        queue.Enqueue(new CopyFileCommand(receiver, "sourcefile.txt", "copyfile.txt"));

        Console.WriteLine("Commands are enqueued. Press any key to exit...");
        Console.ReadKey();

        invoker.StopProcessing();
    }
}

public interface ICommand
{
    void Execute();
}

public class FileOperationReceiver
{
    public void FtpDownload(string filename)
    {
        Console.WriteLine($"Downloading {filename} via FTP.");
    }

    public void HttpDownload(string url)
    {
        Console.WriteLine($"Downloading from {url} via HTTP.");
    }

    public void CreateAndFillFile(string filename, int size)
    {
        Console.WriteLine($"Creating and filling {filename} with {size} bytes of random data.");
    }

    public void CopyFile(string sourceFilename, string destinationFilename)
    {
        Console.WriteLine($"Copying file from {sourceFilename} to {destinationFilename}.");
    }
}

public class FtpDownloadCommand : ICommand
{
    private readonly FileOperationReceiver _receiver;
    private readonly string _filename;

    public FtpDownloadCommand(FileOperationReceiver receiver, string filename)
    {
        _receiver = receiver;
        _filename = filename;
    }

    public void Execute()
    {
        _receiver.FtpDownload(_filename);
    }
}

public class HttpDownloadCommand : ICommand
{
    private readonly FileOperationReceiver _receiver;
    private readonly string _url;

    public HttpDownloadCommand(FileOperationReceiver receiver, string url)
    {
        _receiver = receiver;
        _url = url;
    }

    public void Execute()
    {
        _receiver.HttpDownload(_url);
    }
}

public class CreateAndFillFileCommand : ICommand
{
    private readonly FileOperationReceiver _receiver;
    private readonly string _filename;
    private readonly int _size;

    public CreateAndFillFileCommand(FileOperationReceiver receiver, string filename, int size)
    {
        _receiver = receiver;
        _filename = filename;
        _size = size;
    }

    public void Execute()
    {
        _receiver.CreateAndFillFile(_filename, _size);
    }
}

public class CopyFileCommand : ICommand
{
    private readonly FileOperationReceiver _receiver;
    private readonly string _sourceFilename;
    private readonly string _destinationFilename;

    public CopyFileCommand(FileOperationReceiver receiver, string sourceFilename, string destinationFilename)
    {
        _receiver = receiver;
        _sourceFilename = sourceFilename;
        _destinationFilename = destinationFilename;
    }

    public void Execute()
    {
        _receiver.CopyFile(_sourceFilename, _destinationFilename);
    }
}

public class CommandInvoker
{
    private readonly ConcurrentQueue<ICommand> _queue;
    private readonly Thread[] _workers;
    private bool _continueProcessing = true;

    public CommandInvoker(ConcurrentQueue<ICommand> queue)
    {
        _queue = queue;
        _workers = new Thread[2] { new Thread(Process), new Thread(Process) };
    }

    public void StartProcessing()
    {
        foreach (var worker in _workers)
        {
            worker.Start();
        }
    }

    private void Process()
    {
        while (_continueProcessing)
        {
            if (_queue.TryDequeue(out var command))
            {
                command.Execute();
            }
            else
            {
                Thread.Sleep(100);
            }
        }
    }

    public void StopProcessing()
    {
        _continueProcessing = false;
        foreach (var worker in _workers)
        {
            worker.Join();
        }
    }
}
