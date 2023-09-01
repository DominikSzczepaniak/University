using System.Reflection;

public class ResourceExtractor
{
    public static void ExtractResourceToFile(string resourceName, string outputPath)
    {
        Assembly assembly = Assembly.GetExecutingAssembly();

        using (Stream resourceStream = assembly.GetManifestResourceStream(resourceName))
        {
            if (resourceStream == null)
            {
                throw new ArgumentException($"Resource '{resourceName}' not found in the assembly.");
            }

            using (FileStream fileStream = new FileStream(outputPath, FileMode.Create))
            {
                resourceStream.CopyTo(fileStream);
            }
        }
    }
}

// Path: 9.6\Program.cs
class Program
{
    static void Main(string[] args)
    {
        ResourceExtractor.ExtractResourceToFile("C:\\Users\\szcze\\Desktop\\sharing mac\\9.6\\9.6\\plik.txt", "C:\\Users\\szcze\\Desktop\\sharing mac\\9.6\\9.6\\wyjscie.txt");
    }
}