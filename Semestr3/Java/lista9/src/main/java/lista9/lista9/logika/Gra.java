package lista9.lista9.logika;

import lista9.lista9.obiekty.*;

import java.util.Random;

public class Gra{
    public Plansza planszaGry;
    private final int ILOSC_DZIECI;
    public Gra(int n, int m){
        Random generator = new Random();
        ILOSC_DZIECI = generator.nextInt(7)+10;
        planszaGry = new Plansza(n, m);
        planszaGry.wygenerujDzieci(ILOSC_DZIECI);
        planszaGry.wygenerujMikolaja(ILOSC_DZIECI);
    }
}
