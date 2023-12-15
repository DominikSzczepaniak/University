package obliczenia;

public class Liczba extends Wyrazenie{
    private double wartosc;
    public Liczba(double arg){
        this.wartosc = arg;
    }

    @Override
    public double licz() {
        return wartosc;
    }

    @Override
    public String toString() {
        return Double.toString(wartosc);
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof Liczba)) return false;
        Liczba c = (Liczba) obj;
        double w1 = this.licz();
        double w2 = c.licz();
        return w1 == w2;
    }
}
