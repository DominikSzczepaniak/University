package obliczenia;

public class Odejmowanie extends Wyrazenie{
    Wyrazenie lewe;
    Wyrazenie prawe;
    public Odejmowanie(Wyrazenie l, Wyrazenie p){
        lewe = l;
        prawe = p;
    }

    @Override
    public double licz() {
        double wynikLewy = lewe.licz();
        double wynikPrawy = prawe.licz();
        return wynikLewy-wynikPrawy;
    }

    @Override
    public String toString() {
        return "Odejmowanie{" +
                "lewe=" + lewe +
                ", prawe=" + prawe +
                '}';
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof Odejmowanie)) return false;
        Odejmowanie c = (Odejmowanie) obj;
        double w1 = this.licz();
        double w2 = c.licz();
        return w1 == w2;
    }
}
