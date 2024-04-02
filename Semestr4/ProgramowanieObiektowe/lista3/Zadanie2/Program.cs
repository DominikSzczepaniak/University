class Program
{
    static void Main(string[] args)
    {
        MyDictionary<string, int> dictionary = new MyDictionary<string, int>();

        dictionary.Add("one", 1);
        dictionary.Add("two", 2);
        dictionary.Add("three", 3);

        Console.WriteLine("Czy słownik zawiera klucz 'one'? {0}", dictionary.ContainsKey("one")); // true

        int value = dictionary.Find("two");
        Console.WriteLine("Wartość dla klucza 'two': {0}", value); // 2

        dictionary.Remove("three");

        try
        {
            value = dictionary.Find("three");
            Console.WriteLine("Wartość dla klucza 'three': {0}", value); // KeyNotFoundException
        }
        catch (KeyNotFoundException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }
}