class Program
{
    public static void Main()
    {
        var item1 = new { Field1 = "The value", Field2 = 5 };
        var item2 = new { Field1 = "Another value", Field2 = 10 };
        List<object> theList = new List<object>();
        theList.Add(item1);
        theList.Add(item2);
        
    }
}