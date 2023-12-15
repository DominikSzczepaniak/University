package obliczenia;

public class Logarytm extends Wyrazenie{
    private Wyrazenie wartosc;
    private Wyrazenie podstawa;
    public Logarytm(Wyrazenie podstawa, Wyrazenie wartosc){
        this.wartosc = wartosc;
        this.podstawa = podstawa;
    }

    @Override
    public double licz() {
        return Math.log(wartosc.licz()) / Math.log(podstawa.licz());
    }

    @Override
    public String toString() {
        return "Log" + podstawa.licz() + "(" + wartosc.licz() + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof Logarytm)) return false;
        Logarytm c = (Logarytm) obj;
        double w1 = this.licz();
        double w2 = c.licz();
        return w1 == w2;
    }
}
