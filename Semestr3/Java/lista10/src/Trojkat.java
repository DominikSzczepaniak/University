import java.util.Arrays;

public class Trojkat {
    public double a;
    public double b;
    public double c;

    public Trojkat(double a, double b, double c) {
        if (!czyTrojkat(a, b, c)) {
            throw new IllegalArgumentException("Podane długości boków nie spełniają warunku trójkąta.");
        }
        this.a = a;
        this.b = b;
        this.c = c;
    }

    private boolean czyTrojkat(double a, double b, double c) {
        return (a + b > c) && (a + c > b) && (b + c > a);
    }

    @Override
    public String toString() {
        return a + " " + b + " " + c;
    }
}
