package lista9.lista9.logika;

import lista9.lista9.obiekty.Dziecko;
import lista9.lista9.obiekty.Mikolaj;
import lista9.lista9.obiekty.Plansza;

import java.util.Random;

public class Gra {
    private Plansza planszaGry;
    private Dziecko[] dzieci;
    private Mikolaj mikolaj;
    private final int ILOSC_DZIECI;
    public Gra(int n, int m){
        Random generator = new Random();
        ILOSC_DZIECI = generator.nextInt(7)+10;
        dzieci = new Dziecko[ILOSC_DZIECI];
        planszaGry = new Plansza(n, m);
        planszaGry.wygenerujDzieci(ILOSC_DZIECI);
        planszaGry.wygenerujMikolaja(ILOSC_DZIECI);
    }
}
