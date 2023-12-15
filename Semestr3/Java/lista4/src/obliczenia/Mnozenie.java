package obliczenia;

public class Mnozenie extends Wyrazenie{
    Wyrazenie lewe;
    Wyrazenie prawe;
    public Mnozenie(Wyrazenie l, Wyrazenie p){
        lewe = l;
        prawe = p;
    }

    @Override
    public double licz() {
        double wynikLewy = lewe.licz();
        double wynikPrawy = prawe.licz();
        double odpowiedz = wynikLewy * wynikPrawy;
        return odpowiedz;
    }

    @Override
    public String toString() {
        return "Mnozenie{" +
                "lewe=" + lewe +
                ", prawe=" + prawe +
                '}';
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof Mnozenie)) return false;
        Mnozenie c = (Mnozenie) obj;
        double w1 = this.licz();
        double w2 = c.licz();
        return w1 == w2;
    }
}
