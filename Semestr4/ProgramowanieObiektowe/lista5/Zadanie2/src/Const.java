import java.util.Map;

class Const extends Expression {
    private final int value;

    public Const(int value) {
        this.value = value;
    }

    @Override
    public int evaluate(Map<String, Integer> context) {
        return value;
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }
}

