using System.Dynamic;
using System.Linq.Expressions;

class Program
{

    public static void Main()
    {
        dynamic x = new DynamicExtend(5);
        x.Imie = "jan";
        x.Nazwisko = "kowalski";
        x.ID = "123";
        Console.WriteLine(x.ID);
        Console.WriteLine(x.Imie);
        x[0] = 15;
        x[1] = 16;
        Console.WriteLine(x[0]);
        x(1, "Imie");
        var c = x.GetIndexDictionary();
        Console.WriteLine(c);
        var b = x++;
        Console.WriteLine(b);
        dynamic v = new DynamicExtend(10);
        dynamic z = new DynamicExtend(11);
        dynamic p = (dynamic)v + (dynamic)z;
        Console.WriteLine(p.id);
    }
}

class DynamicExtend : DynamicObject
{
    private Dictionary<string, object> dict = new Dictionary<string, object>();
    private Dictionary<int, object> indexing = new Dictionary<int, object>();
    public int id=0;

    public DynamicExtend(int value)
    {
        this.id = value;
    }
    public override bool TryGetMember(GetMemberBinder binder, out object? result)
    {
        if (dict.ContainsKey(binder.Name))
        {
            result = dict[binder.Name];
            return true;
        }

        result = null;
        return false;
    }

    public override bool TrySetMember(SetMemberBinder binder, object? value)
    {
        if (binder.Name == "Imie")
        {
            dict["Imie"] = value;
            return true;
        }
        if (binder.Name == "Nazwisko")
        {
            dict["Nazwisko"] = value;
            return true;
        }
        if (binder.Name == "ID")
        {
            dict["ID"] = value;
            return true;
        }
        return false;
    }

    public override bool TryGetIndex(GetIndexBinder binder, object[] indexes, out object? result)
    {
        int index = (int)indexes[0];
        if (indexing.ContainsKey(index))
        {
            result = indexing[index];
            return true;
        }

        result = null;
        return false;
    }

    public override bool TrySetIndex(SetIndexBinder binder, object[] indexes, object? value)
    {
        int index = (int)indexes[0];
        indexing[index] = value;
        return true;
    }

    public override bool TryInvoke(InvokeBinder binder, object?[]? args, out object? result)
    {
        if (args.Length == 2)
        {
            result = indexing[(int)args[0]].ToString() + " " + dict[(string)args[1]].ToString();
            return true;
        }

        result = null;
        return false;

    }

    public override bool TryInvokeMember(InvokeMemberBinder binder, object?[]? args, out object? result)
    {
        if (binder.Name == "GetIndexDictionary")
        {
            result = indexing;
            return true;
        }

        if (binder.Name == "GetMemberDictionary")
        {
            result = dict;
            return true;
        }

        result = null;
        return false;
    }

    public override bool TryUnaryOperation(UnaryOperationBinder binder, out object? result)
    {
        switch (binder.Operation)
        {
            case ExpressionType.Increment:
                result = dict.Select(x => x.ToString() + " " + x.ToString());
                return true;
        }

        result = null;
        return false;
    }

    public static DynamicExtend operator +(DynamicExtend a, DynamicExtend b)
    {
        return new DynamicExtend(a.id + b.id);
    }
    public override bool TryBinaryOperation(BinaryOperationBinder binder, object arg, out object? result)
    {
        switch (binder.Operation)
        {
            case ExpressionType.Add:
            {
                result = this + (DynamicExtend)arg;
                return true;
            }
        }

        result = null;
        return false;
    }
}