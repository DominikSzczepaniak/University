package obliczenia;

public abstract class Wyrazenie implements Obliczalny{
    public static double suma(Wyrazenie... wyr){
        double wynik = 0;
        for(Wyrazenie w : wyr){
            wynik += w.licz();
        }
        return wynik;
    }
    public static double iloczyn(Wyrazenie... wyr){
        double wynik = 1;
        for(Wyrazenie w : wyr){
            wynik *= w.licz();
        }
        return wynik;
    }
    //public abstract double licz();
}
