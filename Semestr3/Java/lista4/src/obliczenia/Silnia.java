package obliczenia;

public class Silnia extends Wyrazenie{
    private Wyrazenie wartosc;
    public Silnia(Wyrazenie arg){
        this.wartosc = arg;
    }

    @Override
    public double licz() {
        double ile = wartosc.licz();
        if(ile != Math.floor(ile)){
            Stala.throwException(new Exception("Silnia jest ustalona tylko dla liczb naturalnych"));
        }
        double wynik = 1;
        for(int i = 2; i<=ile; i++){
            wynik *= i;
        }
        return wynik;
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
