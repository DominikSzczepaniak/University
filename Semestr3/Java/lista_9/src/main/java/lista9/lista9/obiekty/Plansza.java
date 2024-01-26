package lista9.lista9.obiekty;

import lista9.lista9.logika.MikolajZnalezionyListener;

import java.util.Random;

public class Plansza{
    private final int wysokosc;
    private final int szerokosc;
    public ObiektNaPlanszy[][] plansza;
    public Mikolaj mikolaj;
    public Dziecko[] dzieci;
    MikolajZnalezionyListener mikolajZnalezionyListener;
    private final Para[] kierunki = {new Para(-1, 0), new Para(1, 0), new Para(0, 1), new Para(0, -1)};
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
                    dzieci[dziecko].szybkosc = 3;
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
        mikolaj.setIloscPaczek(mikolaj.getIloscPaczek()-1);
    }

    public void ruchMikolaja(Para jaki){
        Para pozycjaMikolaja = mikolaj.getPos();
        Para nowaPozycja = ruch(pozycjaMikolaja, jaki);
        mikolaj.setPos(nowaPozycja);
    }

    public Para prezentNaPoluObok(Para pos){
        for(var kierunek : kierunki){
            Para newPos = new Para(pos.getFirst()+ kierunek.getFirst(), pos.getSecond()+kierunek.getSecond());
            if(plansza[newPos.getFirst()][newPos.getSecond()] instanceof Prezent){
                return newPos;
            }
        }
        return null;
    }

    public void dzieckoSzukaPrezent(Dziecko dziecko){
        if(dziecko.znalazlPrezent){
            return;
        }
        if(dziecko.odlegloscDoMikolaja(mikolaj) <= 1){
            dziecko.zauwazylMikolaja = true;
        }
        Para prezentObok = prezentNaPoluObok(dziecko.getPos());
        if(prezentObok != null){
            dziecko.znalazlPrezent = true;
            plansza[prezentObok.getFirst()][prezentObok.getSecond()] = new PustyObiekt();
        }
    }

    public boolean koniecGry(){
        if(mikolaj.getIloscPaczek() == 0){
            for(int i = 0; i<wysokosc; i++){
                for(int j = 0; j<szerokosc; j++){
                    if(plansza[i][j] instanceof Prezent){
                        return false;
                    }
                }
            }
            return true;
        }
        return false;
    }

    public void dzieckoUpdate(Dziecko dziecko){
        if(dziecko.znalazlPrezent){
            return;
        }
        if(dziecko.wTrakcieKroku){
            dziecko.wykonajProgresKroku();
        }
        else{
            //tu musimy sprawdzic czy spi
            if(dziecko.wTrakcieSnu){
                if(dziecko.wykonajProgresSnu()){ //jesli true to dziecko zakonczy sen, w przeciwnym wypadku nic nie robimy
                    dzieckoSzukaPrezent(dziecko);
                    if(dziecko.zauwazylMikolaja){
                        mikolajZnalezionyListener.znalezionoMikolaja();
                    }
                    if(!dziecko.znalazlPrezent){
                        dziecko.ustalKierunek(mikolaj);
                    }
                }
            }
            else{
                if(dziecko.odleglosc == dziecko.ZASIEG_ZMECZENIA){
                    dziecko.dzieckoZasypia();
                    dziecko.wykonajProgresSnu();
                }
            }
        }
    }

    public void setMikolajZnalezionyListener(MikolajZnalezionyListener listener){
        this.mikolajZnalezionyListener = listener;
    }

    public void mikolajUpdate(Mikolaj mikolaj){
        if(mikolaj.wTrakcieKroku){
            mikolaj.wykonajProgresKroku();
        }
        if(!mikolaj.wTrakcieKroku){ //nie chce dawac else bo moze skonczyc krok od razu gdy szybkosc = 1
            mikolaj.poczatekKrokuHelper(mikolaj.kierunekStrzalki);
        }

    }
}
