import java.util.Map;

class Variable extends Expression {
    private final String name;

    public Variable(String name) {
        this.name = name;
    }

    @Override
    public int evaluate(Map<String, Integer> context) {
        if (context.containsKey(name)) {
            return context.get(name);
        }
        throw new IllegalArgumentException("Undefined variable: " + name);
    }

    @Override
    public String toString() {
        return name;
    }
}