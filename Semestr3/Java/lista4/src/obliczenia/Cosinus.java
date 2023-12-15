package obliczenia;

public class Cosinus extends Wyrazenie{
    private final Wyrazenie argument;
    public Cosinus(Wyrazenie arg){
        this.argument = arg;
    }

    @Override
    public double licz() {
        return Math.cos(argument.licz());
    }

    @Override
    public String toString() {
        return Double.toString(Math.cos(argument.licz()));
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof Cosinus)) return false;
        Cosinus c = (Cosinus) obj;
        double w1 = this.licz();
        double w2 = c.licz();
        return w1 == w2;
    }
}
