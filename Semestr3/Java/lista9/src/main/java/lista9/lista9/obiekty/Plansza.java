package lista9.lista9.obiekty;

import lista9.lista9.logika.RuchListener;

import java.util.Random;

public class Plansza{
    private final int wysokosc;
    private final int szerokosc;
    public ObiektNaPlanszy[][] plansza;
    Mikolaj mikolaj;
    Dziecko[] dzieci;
    private Para[] kierunki = {new Para(-1, 0), new Para(1, 0), new Para(0, 1), new Para(0, -1)};
    public Plansza(int n, int m){
        if(n<10 || m<10){
            throw new IllegalStateException("Plansza musi miec wymiary przynajmniej 10x10");
        }
        wysokosc = n;
        szerokosc = m;
        plansza = new ObiektNaPlanszy[n][m];
    }
    public Para ruch(Para skad, Para krok){
        return new Para((skad.getFirst() + krok.getFirst())%wysokosc, (skad.getSecond()+krok.getSecond())%szerokosc);
    }

    public void wygenerujDzieci(int ilosc){
        Random generator = new Random();
        dzieci = new Dziecko[ilosc];
        for(int dziecko = 0; dziecko<ilosc; dziecko++){
            while(true){
                int y = generator.nextInt(wysokosc);
                int x = generator.nextInt(szerokosc);
                if(moznaZrespic(new Para(y, x))){
                    plansza[y][x] = dzieci[dziecko];
                    break;
                }
            }
        }
    }

    public void wygenerujMikolaja(int iloscDzieci){
        Random generator = new Random();
        while(true){
            int y = generator.nextInt(wysokosc);
            int x = generator.nextInt(szerokosc);
            if(moznaZrespic(new Para(y, x))){
                mikolaj = new Mikolaj(iloscDzieci);
                plansza[y][x] = mikolaj;
                mikolaj.setPos(new Para(y, x));
                break; //<- tu lepiej returna?
            }
        }
    }

    public boolean moznaZrespic(Para gdzie){
        if(!(plansza[gdzie.getFirst()][gdzie.getSecond()] instanceof PustyObiekt)){
            return false;
        }
        for(var kierunek : kierunki){
            if(!(plansza[gdzie.getFirst()+kierunek.getFirst()][gdzie.getSecond()+kierunek.getSecond()] instanceof PustyObiekt)){
                return false;
            }
        }
        return true;
    }

    public void mikolajPolozylPrezent() {
        plansza[mikolaj.getPos().getFirst()][mikolaj.getPos().getSecond()] = new Prezent();
    }

    public void ruchMikolaja(Para jaki){
        Para pozycjaMikolaja = mikolaj.getPos();
        Para nowaPozycja = ruch(pozycjaMikolaja, jaki);
        mikolaj.setPos(nowaPozycja);
    }
}
