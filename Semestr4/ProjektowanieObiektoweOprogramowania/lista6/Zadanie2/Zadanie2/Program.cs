using System;
using System.Collections.Generic;

public class Context
{
    private Dictionary<string, bool> variables = new Dictionary<string, bool>();

    public bool GetValue(string variableName)
    {
        if (variables.ContainsKey(variableName))
        {
            return variables[variableName];
        }
        else
        {
            throw new Exception($"Variable '{variableName}' not defined.");
        }
    }

    public void SetValue(string variableName, bool value)
    {
        variables[variableName] = value;
    }
}

public abstract class AbstractExpression
{
    public abstract bool Interpret(Context context);
}

public class ConstExpression : AbstractExpression
{
    private bool value;

    public ConstExpression(bool value)
    {
        this.value = value;
    }

    public override bool Interpret(Context context)
    {
        return value;
    }
}

public class VariableExpression : AbstractExpression
{
    private string name;

    public VariableExpression(string name)
    {
        this.name = name;
    }

    public override bool Interpret(Context context)
    {
        return context.GetValue(name);
    }
}

public class BinaryExpression : AbstractExpression
{
    private AbstractExpression left;
    private AbstractExpression right;
    private Func<bool, bool, bool> operation;

    public BinaryExpression(AbstractExpression left, AbstractExpression right, Func<bool, bool, bool> operation)
    {
        this.left = left;
        this.right = right;
        this.operation = operation;
    }

    public override bool Interpret(Context context)
    {
        bool leftResult = left.Interpret(context);
        bool rightResult = right.Interpret(context);
        return operation(leftResult, rightResult);
    }
}

public class UnaryExpression : AbstractExpression
{
    private AbstractExpression expression;
    private Func<bool, bool> operation;

    public UnaryExpression(AbstractExpression expression, Func<bool, bool> operation)
    {
        this.expression = expression;
        this.operation = operation;
    }

    public override bool Interpret(Context context)
    {
        bool result = expression.Interpret(context);
        return operation(result);
    }
}

class Program
{
    static void Main()
    {
        Context ctx = new Context();
        ctx.SetValue("x", false);
        ctx.SetValue("y", true);

        AbstractExpression x = new VariableExpression("x");
        AbstractExpression y = new VariableExpression("y");
        AbstractExpression notX = new UnaryExpression(x, b => !b);
        AbstractExpression xAndY = new BinaryExpression(x, y, (a, b) => a && b);
        AbstractExpression expression = new BinaryExpression(notX, y, (a, b) => a || b);

        bool value = expression.Interpret(ctx);
        Console.WriteLine(value);  // Output will be true
    }
}
