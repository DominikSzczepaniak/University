package obliczenia;

public class Wymierna implements Comparable<Wymierna>{
    private int licznik, mianownik = 1;
    public Wymierna(){
        licznik = 0;
    }
    public Wymierna(int n){
        licznik = n;
    }
    public Wymierna(int n, int m){
        if(m == 0){
            throw new IllegalArgumentException("Mianownik nie moze byc 0!");
        }
        if(m < 0){
            m *= -1;
            n *= -1;
        }
        int nwd = euklides(Math.abs(n), Math.abs(m));
        n /= nwd;
        m /= nwd;
        licznik = n;
        mianownik = m;
    }

    public int getLicznik() {
        return licznik;
    }

    public int getMianownik() {
        return mianownik;
    }

    @Override
    public String toString() {
        return licznik + "/" + mianownik;
    }

    @Override
    public boolean equals(Object obj) {
        if(obj == this) return true;
        if(obj == null || !(obj instanceof Wymierna)) return false;
        Wymierna liczba2 = (Wymierna) obj;
        if(liczba2.licznik == this.licznik && liczba2.mianownik==this.mianownik){
            return true;
        }
        return false;
    }

    private static int euklides(int a, int b){
        if(b==0){
            return a;
        }
        return euklides(b, a%b);
    }

    @Override
    public int compareTo(Wymierna o) {
        return Integer.compare(licznik * o.mianownik, o.licznik * mianownik);
    }

    public static Wymierna dodaj(Wymierna a, Wymierna b) {
        int nowyLicznik = a.licznik * b.mianownik + b.licznik * a.mianownik;
        int nowyMianownik = a.mianownik * b.mianownik;
        return new Wymierna(nowyLicznik, nowyMianownik);
    }

    public static Wymierna odejmij(Wymierna a, Wymierna b) {
        int nowyLicznik = a.licznik * b.mianownik - b.licznik * a.mianownik;
        int nowyMianownik = a.mianownik * b.mianownik;
        return new Wymierna(nowyLicznik, nowyMianownik);
    }

    public static Wymierna pomnoz(Wymierna a, Wymierna b) {
        int nowyLicznik = a.licznik * b.licznik;
        int nowyMianownik = a.mianownik * b.mianownik;
        return new Wymierna(nowyLicznik, nowyMianownik);
    }

    public static Wymierna podziel(Wymierna a, Wymierna b) {
        if (b.licznik == 0) {
            throw new ArithmeticException("Dzielenie przez 0.");
        }
        int nowyLicznik = a.licznik * b.mianownik;
        int nowyMianownik = a.mianownik * b.licznik;
        return new Wymierna(nowyLicznik, nowyMianownik);
    }
    public static double log2(double a){
        return Math.log(a) / Math.log(2);
    }
}
