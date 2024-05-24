public class PrintExpressionVisitor : ExpressionVisitor
{
    protected override Expression VisitBinary(BinaryExpression expression)
    {
        Console.WriteLine("Binary Expression: {0} {1} {2}", expression.Left, expression.NodeType, expression.Right);
        return base.VisitBinary(expression);
    }

    protected override Expression VisitLambda<T>(Expression<T> expression)
    {
        Console.WriteLine("Lambda Expression: {0} -> {1}",
            expression.Parameters.Aggregate(string.Empty, (acc, param) => acc + (acc == string.Empty ? "" : ", ") + param.Name),
            expression.Body);
        return base.VisitLambda(expression);
    }

    protected override Expression VisitConstant(ConstantExpression expression)
    {
        Console.WriteLine("Constant Expression: {0}", expression.Value);
        return base.VisitConstant(expression);
    }

    protected override Expression VisitConditional(ConditionalExpression expression)
    {
        Console.WriteLine("Conditional Expression: {0} ? {1} : {2}", expression.Test, expression.IfTrue, expression.IfFalse);
        return base.VisitConditional(expression);
    }

    protected override Expression VisitMethodCall(MethodCallExpression expression)
    {
        Console.WriteLine("Method Call Expression: {0}.{1}({2})",
            expression.Object,
            expression.Method.Name,
            string.Join(", ", expression.Arguments.Select(arg => arg.ToString())));
        return base.VisitMethodCall(expression);
    }
}