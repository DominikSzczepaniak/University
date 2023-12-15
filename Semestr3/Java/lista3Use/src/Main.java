import lista3_klasy.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Punkt p1 = new Punkt(1, 1);
        Punkt p2 = new Punkt(2, 2);
        Punkt p3 = new Punkt(0, 4);
        //trojkat testy
        Trojkat abc = new Trojkat(p1,p2,p3);
        Prosta r = new Prosta(-10,0,0);
        abc.wypisz();
        abc.odbij(r);
        abc.wypisz();
        abc.przesun(new Wektor(5, 5));
        abc.wypisz();
        abc.obroc(new Punkt(0,0), 180);
        abc.wypisz();
        System.out.println("KONIEC TROJKAT");
        //odcinek
        Punkt p4 = new Punkt(0, 0);
        Punkt p5 = new Punkt(0, 5);
        Odcinek ab = new Odcinek(p4, p4);

        Punkt d = new Punkt(0, 0);
        Punkt e = new Punkt(0, 0);
        Odcinek xy = new Odcinek(d, e);


        ab.wypisz();
        ab.obroc(new Punkt(0,0), 90);
        ab.wypisz();
        ab.przesun(new Wektor(5, 5));
        ab.wypisz();
        ab.odbij(new Prosta(1, 1, 1));
        ab.wypisz();
        System.out.println("KONIEC ODCINEK");
        //Punkt
        Punkt a = new Punkt(4, 4);
        a.przesun(new Wektor(-4, -4));
        a.wypisz();
        a.odbij(new Prosta(1, 0, 4));
        a.wypisz();
        a.obroc(new Punkt(0, 0), 234);
        a.wypisz();
    }
}