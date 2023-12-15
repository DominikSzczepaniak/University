package obliczenia;

public class Sinus extends Wyrazenie{
    private final Wyrazenie argument;
    public Sinus(Wyrazenie arg){
        this.argument = arg;
    }

    @Override
    public double licz() {
        return Math.sin(argument.licz());
    }

    @Override
    public String toString() {
        return Double.toString(Math.sin(argument.licz()));
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof Sinus)) return false;
        Sinus c = (Sinus) obj;
        double w1 = this.suma();
        double w2 = c.suma();
        return w1 == w2;
    }
}
