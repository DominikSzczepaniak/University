using System;
using System.Text;

class Program
{
    private static void fileStreamUse(string Path)
    {
        using(FileStream fs = new FileStream(Path, FileMode.OpenOrCreate))
        {
            byte[] bytes = new byte[fs.Length];
            fs.Read(bytes, 0, bytes.Length);
            string textFromFile = System.Text.Encoding.Default.GetString(bytes);
            Console.WriteLine(textFromFile);
        }   
    }
    private static void streamReaderUse(string Path)
    {
        using (StreamReader sr = new StreamReader(Path))
        {
            Console.WriteLine(sr.ReadToEnd());
        }
    }
    private static void streamWriterUse(string Path)
    {
        using(StreamWriter sw = new StreamWriter(Path, true, System.Text.Encoding.Default))
        {
            sw.WriteLine("Hello World");
        }
    }

    private static void binaryReaderUse(string Path)
    {
        using(BinaryReader br = new BinaryReader(File.Open(Path, FileMode.Open)))
        {
            Console.WriteLine(br.ReadString());
        }
    }
    private void binaryWriterUse(string Path)
    {
        using(BinaryWriter bw = new BinaryWriter(File.Open(Path, FileMode.OpenOrCreate)))
        {
            bw.Write("Hello World");
        }

    }
    private static void stringBuilderUse(string Path)
    {
        StringBuilder sb = new StringBuilder();
        sb.Append("Hello World");
        sb.AppendLine("Hello World");
        sb.AppendFormat("{0} {1}", "Hello", "World");
        sb.Remove(0, 5);
        sb.Insert(0, "Hello");
        Console.WriteLine(sb.ToString());
        
    }   

    private static void stringReaderUse(string Path)
    {
        using(StringReader sr = new StringReader(Path))
        {
            Console.WriteLine(sr.ReadToEnd());
        }
    }
    static void Main(string[] args)
    {
        Console.WriteLine("===================================");
        fileStreamUse("test.txt");
        Console.WriteLine("===================================");
        streamReaderUse("test.txt");
        Console.WriteLine("===================================");
        streamWriterUse("test.txt");
        Console.WriteLine("===================================");
        binaryReaderUse("test.txt");
        Console.WriteLine("===================================");
        stringBuilderUse("test.txt");
        Console.WriteLine("===================================");
        stringReaderUse("test.txt");
        Console.WriteLine("===================================");
    }
}   
