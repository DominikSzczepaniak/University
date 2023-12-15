package obliczenia;

public class Odwrotnosc extends Wyrazenie{
    private Wyrazenie wartosc;
    public Odwrotnosc(Wyrazenie arg){
        this.wartosc = arg;
    }

    @Override
    public double licz() {
        return 1 / wartosc.licz();
    }

    @Override
    public String toString() {
        return "1/" + wartosc.licz();
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof Odwrotnosc)) return false;
        Odwrotnosc c = (Odwrotnosc) obj;
        double w1 = this.licz();
        double w2 = c.licz();
        return w1 == w2;
    }
}
