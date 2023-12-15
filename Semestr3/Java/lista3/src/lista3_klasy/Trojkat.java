package lista3_klasy;

public class Trojkat {
    public Trojkat(Punkt a, Punkt b, Punkt c){
        if(a == b || a == c || b == c){
            throw new IllegalArgumentException("Do stworzenia trójkąta potrzebujemy 3 różne punkty");
        }
        else if(Punkt.wspolliniowe(a,b,c)){
            throw new IllegalArgumentException("Punkty nie mogą być współliniowe");
        }
        w1 = a;
        w2 = b;
        w3 = c;
    }
    public void obroc(Punkt p, double kat){
        double radiany = Math.toRadians(kat);
        double cosinus = Math.cos(radiany);
        double sinus = Math.sin(radiany);
        Punkt[] punkty = {w1,w2,w3};
        Odcinek.obracaniePuntkow(p, cosinus, sinus, punkty);
    }
    public void przesun(Wektor v){
        w1.przesun(v);
        w2.przesun(v);
        w3.przesun(v);
    }
    public void wypisz(){
        w1.wypisz();
        w2.wypisz();
        w3.wypisz();
    }
    public void odbij(Prosta r) throws Exception {
        this.w1.odbij(r);
        this.w2.odbij(r);
        this.w3.odbij(r);
    }
    private Punkt w1;
    private Punkt w2;
    private Punkt w3;
}

