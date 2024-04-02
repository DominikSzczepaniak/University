// Dominik Szczepaniak
// lista 5 zadanie 2
// javac 21.0.2
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> context = new HashMap<>();
        context.put("x", 5);

        Expression expr = new Add(new Const(4), new Variable("x"));
        Expression complexExpr = new Multiply(expr, new Const(2));

        System.out.println("Expression: " + expr + " = " + expr.evaluate(context));
        System.out.println("Complex Expression: " + complexExpr + " = " + complexExpr.evaluate(context));
    }
}