import lista3_klasy.*;
public class Main {
    public static void main(String[] args) throws Exception {
        Punkt p1 = new Punkt(1, 1);
        Punkt p2 = new Punkt(2, 2);
        Punkt p3 = new Punkt(0, 4);
        Trojkat abc = new Trojkat(p1,p2,p3);
        Prosta r = new Prosta(-10,0,0);
        abc.wypisz();
        abc.odbij(r);
        abc.wypisz();
    }
}