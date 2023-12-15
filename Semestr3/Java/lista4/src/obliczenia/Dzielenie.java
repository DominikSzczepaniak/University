package obliczenia;

public class Dzielenie extends Wyrazenie{
    Wyrazenie lewe;
    Wyrazenie prawe;
    public Dzielenie(Wyrazenie l, Wyrazenie p){
        lewe = l;
        prawe = p;
    }

    @Override
    public double licz() {
        double wynikLewy = lewe.licz();
        double wynikPrawy = prawe.licz();
        if(wynikPrawy == 0){
            Stala.throwException(new Exception("Dzielenie przez 0"));
        }
        return wynikLewy/wynikPrawy;
    }

    @Override
    public String toString() {
        return "Dzielenie{" +
                "lewe=" + lewe +
                ", prawe=" + prawe +
                '}';
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof Dzielenie)) return false;
        Dzielenie c = (Dzielenie) obj;
        double w1 = this.licz();
        double w2 = c.licz();
        return w1 == w2;
    }
}
