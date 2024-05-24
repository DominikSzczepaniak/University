using System;
using System.IO;

public interface ILogger
{
    void Log(string message);
}

public class ConsoleLogger : ILogger
{
    public void Log(string message)
    {
        Console.WriteLine(message);
    }
}

public class FileLogger : ILogger
{
    private string _filePath;

    public FileLogger(string filePath)
    {
        _filePath = filePath;
    }

    public void Log(string message)
    {
        using (StreamWriter writer = new StreamWriter(_filePath, true))
        {
            writer.WriteLine(message);
        }
    }
}

public class NullLogger : ILogger
{
    public void Log(string message)
    {
    }
}

public enum LogType { None, Console, File }

public class LoggerFactory
{
    private static readonly LoggerFactory _instance = new LoggerFactory();

    private LoggerFactory() { }

    public static LoggerFactory Instance
    {
        get { return _instance; }
    }

    public ILogger GetLogger(LogType logType, string parameters = null)
    {
        switch (logType)
        {
            case LogType.Console:
                return new ConsoleLogger();
            case LogType.File:
                if (parameters == null)
                {
                    throw new ArgumentNullException("For File Logger, file path must be provided.");
                }
                return new FileLogger(parameters);
            case LogType.None:
                return new NullLogger();
            default:
                throw new NotSupportedException("Invalid log type specified.");
        }
    }
}

class Program
{
    static void Main()
    {
        ILogger logger1 = LoggerFactory.Instance.GetLogger(LogType.File, "foo.txt");
        logger1.Log("foo bar");

        ILogger logger2 = LoggerFactory.Instance.GetLogger(LogType.Console);
        logger2.Log("qux");
    }
}