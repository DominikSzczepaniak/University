using System.Text;

class Program
{
    private static void filestreamuse(string fileName)
    {
        try
        {
            using (FileStream fileStream = File.OpenRead(fileName))
            {
                byte[] b = new byte[1024];
                UTF8Encoding temp = new UTF8Encoding(true);
                int readLen;
                while ((readLen = fileStream.Read(b, 0, b.Length)) > 0)
                {
                    Console.WriteLine(temp.GetString(b, 0, readLen));
                }
            }
        }
        catch (Exception e)
        {
            Console.WriteLine("Brak pliku");
            Console.WriteLine(e.Message);
        }
    }

    private static void streamreaderuse(string fileName)
    {
        try
        {
            using (StreamReader streamReader = new StreamReader(fileName))
            {
                string line;
                while ((line = streamReader.ReadLine()) != null)
                {
                    Console.WriteLine(line);
                }
            }
        }
        catch (Exception e)
        {
            Console.WriteLine("Brak pliku");
            Console.WriteLine(e.Message);
        }
    }

    private static void streamWriteruse()
    {
        DirectoryInfo[] cDirs = new DirectoryInfo(@"/").GetDirectories();
        using (StreamWriter sw = new StreamWriter("CDriveDirs.txt"))
        {
            foreach (DirectoryInfo dir in cDirs)
            {
                sw.WriteLine(dir.Name);
            }
        }
        string line = "";
        using (StreamReader sr = new StreamReader("CDriveDirs.txt"))
        {
            while ((line = sr.ReadLine()) != null)
            {
                Console.WriteLine(line);
            }
        }
    }

    private static void binaryReaderUse()
    {
        
    }
    

    private static void binaryWriterUse()
    {
        
    }
    
    
    private static void StringBuilderUse()
    {
        StringBuilder asd = new StringBuilder("qwerwqerqwer");
        string dsa = "asdasdasd";
        asd[1] = 'c';
        //dsa[1] = 'c'; <- error 
        
    }
    
    
    private static void StringWriterUse()
    {
        
    }
    
    public static void Main()
    {
        streamWriteruse();
        StringBuilderUse();



    }
}