package obliczenia;

import struktury.ZbiorTablicowy;

public class Zmienna extends Wyrazenie{
    public final ZbiorTablicowy zmienne;
    private double wartosc;
    private String nazwa;
    public Zmienna(ZbiorTablicowy c, String zmienna){
        this.zmienne = c;
        nazwa = zmienna;
        wartosc = zmienne.szukaj(zmienna).getWartosc();
    }

    @Override
    public double licz() {
        return wartosc;
    }
    @Override
    public String toString() {
        return nazwa;
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof Zmienna)) return false;
        Zmienna c = (Zmienna) obj;
        double w1 = this.licz();
        double w2 = c.licz();
        return w1 == w2;
    }
}
