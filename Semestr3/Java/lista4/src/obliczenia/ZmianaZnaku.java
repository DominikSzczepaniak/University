package obliczenia;

public class ZmianaZnaku extends Wyrazenie{
    private Wyrazenie wartosc;
    public ZmianaZnaku(Wyrazenie arg){
        this.wartosc = arg;
    }

    @Override
    public double licz() {
        return -1 * wartosc.licz();
    }

    @Override
    public String toString() {
        return "-" + wartosc.toString();
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof ZmianaZnaku)) return false;
        ZmianaZnaku c = (ZmianaZnaku) obj;
        double w1 = this.licz();
        double w2 = c.licz();
        return w1 == w2;
    }
}
