public abstract class DataAccessHandler
{
    public void Execute()
    {
        Connect();
        FetchData();
        ProcessData();
        CloseConnection();
    }

    protected abstract void Connect();
    protected abstract void FetchData();
    protected abstract void ProcessData();
    protected abstract void CloseConnection();
}

public class DatabaseDataHandler : DataAccessHandler
{
    protected override void Connect()
    {
        Console.WriteLine("Connecting to database...");
    }

    protected override void FetchData()
    {
        Console.WriteLine("Fetching data...");
    }

    protected override void ProcessData()
    {
        Console.WriteLine("Processing data...");
        // Załóżmy, że mamy już dane jako DataTable
        // DataTable data = ...;
        // int sum = data.AsEnumerable().Sum(row => row.Field<int>("ColumnName"));
        // Console.WriteLine($"Sum of column 'ColumnName': {sum}");
    }

    protected override void CloseConnection()
    {
        Console.WriteLine("Closing connection...");
    }
}


public class XmlDataHandler : DataAccessHandler
{
    protected override void Connect()
    {
        Console.WriteLine("Opening XML file...");
    }

    protected override void FetchData()
    {
        Console.WriteLine("Fetching XML data...");
    }

    protected override void ProcessData()
    {
        Console.WriteLine("Processing XML data...");
        // Załóżmy, że mamy już załadowany XmlDocument
        // XmlDocument xmlDoc = ...;
        // var longestNode = xmlDoc.DocumentElement.ChildNodes.Cast<XmlNode>()
        //                       .OrderByDescending(node => node.Name.Length)
        //                       .FirstOrDefault();
        // Console.WriteLine($"Longest node name: {longestNode?.Name}");
    }

    protected override void CloseConnection()
    {
        Console.WriteLine("Closing XML file...");
    }
}


class Program
{
    static void Main()
    {
        DataAccessHandler databaseHandler = new DatabaseDataHandler();
        DataAccessHandler xmlHandler = new XmlDataHandler();

        databaseHandler.Execute();

        xmlHandler.Execute();
    }
}
