import java.util.Map;

public abstract class Expression {
    public abstract int evaluate(Map<String, Integer> context);
    public abstract String toString();
}
