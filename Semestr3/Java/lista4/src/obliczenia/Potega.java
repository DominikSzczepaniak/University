package obliczenia;

public class Potega extends Wyrazenie{
    private Wyrazenie podstawa;
    private Wyrazenie wykladnik;
    public Potega(Wyrazenie a, Wyrazenie b){
        this.wykladnik = b;
        this.podstawa = a;
    }

    @Override
    public double licz() {
        return Math.pow(podstawa.licz(), wykladnik.licz());
    }

    @Override
    public String toString() {
        return podstawa.licz() + "^" + wykladnik.licz();
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof Potega)) return false;
        Potega c = (Potega) obj;
        double w1 = this.licz();
        double w2 = c.licz();
        return w1 == w2;
    }
}
