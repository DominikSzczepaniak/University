using System.ComponentModel;
using System.Dynamic;

class Program
{
    public Task<int> LongOperation()
    {
        return Task.Delay(3000)
            .ContinueWith(t =>
            {
                return 123;
            });
    }
    
    public async Task<int> LongOperation2()
    {
        await Task.Delay(3000);
        return 123;
    }
    
    
    public static void Taski()
    {
        Task.Delay(3000);
        Task.Run(expObj()); 
        //przy Task.Run tworzy sie nowy watek
    }
    public static dynamic expObj()
    {
        dynamic d = new ExpandoObject();
        d.Name = "Jan";
        d.id = "123";
        d.address = new ExpandoObject();
        d.address.City = "wroclaw";
        IDictionary<string, object> dict = d as IDictionary<string, object>;
        Console.WriteLine(dict.Keys);
        return d;
    }
    public static dynamic DoWork(dynamic x)
    {
        x.Foo(1234);
        
        return x.Foo(1);
    }
    public static void Main()
    {
        Console.WriteLine(DoWork(new ExampleClass()));
    }

}

public class ExampleClass : DynamicObject{
    public override bool TryInvokeMember(InvokeMemberBinder binder, object?[]? args, out object? result)
    {
        if (binder.Name == "Foo")
        {
            result = 1;
            return true;
        }
        else
        {
            result = null;
            return false;
        }
    }

    public override bool TrySetMember(SetMemberBinder binder, object? value)
    {
        return base.TrySetMember(binder, value);
    }

    public override bool TryInvoke(InvokeBinder binder, object?[]? args, out object? result)
    {
        return base.TryInvoke(binder, args, out result);
    }
}