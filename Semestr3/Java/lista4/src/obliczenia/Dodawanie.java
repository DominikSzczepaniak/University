package obliczenia;

public class Dodawanie extends Wyrazenie{
    Wyrazenie lewe;
    Wyrazenie prawe;
    public Dodawanie(Wyrazenie l, Wyrazenie p){
        lewe = l;
        prawe = p;
    }

    @Override
    public double licz() {
        double wynikLewy = lewe.licz();
        double wynikPrawy = prawe.licz();
        return wynikLewy+wynikPrawy;
    }

    @Override
    public String toString() {
        return "Dodawanie{" +
                "lewe=" + lewe +
                ", prawe=" + prawe +
                '}';
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof Dodawanie)) return false;
        Dodawanie c = (Dodawanie) obj;
        double w1 = this.licz();
        double w2 = c.licz();
        return w1 == w2;
    }
}
