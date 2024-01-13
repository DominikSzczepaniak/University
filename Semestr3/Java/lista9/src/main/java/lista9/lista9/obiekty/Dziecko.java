package lista9.lista9.obiekty;

import java.util.Random;

public class Dziecko extends ObiektNaPlanszy {
    public final int ZASIEG_WZROKU = 5;
    public final int ZASIEG_ZMECZENIA = 3;
    public final int CZAS_SNU = 5; //czas jest podany w x * 0.4 (co cykl sprawdzania odejmujemy jeden)
    public boolean znalazlPrezent = false;
    public boolean zauwazylMikolaja = false;
    public boolean wTrakcieSnu = false;
    public int progresSnu = 0;
    Random generator = new Random();
    public void dzieckoZasypia(){

        wTrakcieSnu = true;
        progresSnu = generator.nextInt(5)+3;
    }
    public boolean wykonajProgresSnu(){ //zwraca true jesli sen sie skonczyl
        if(!wTrakcieSnu){
            return false;
        }
        progresSnu--;
        if(progresSnu == 0){
            wTrakcieSnu = false;
            return true;
        }
        return false;

    }

    public int odlegloscDoMikolaja(Mikolaj mikolaj){
        return Math.abs(mikolaj.getPos().getFirst() - getPos().getFirst()) + Math.abs(mikolaj.getPos().getSecond() - getPos().getSecond());
    }

    public void ustalKierunek(Mikolaj mikolaj){
        if(odlegloscDoMikolaja( mikolaj) > ZASIEG_WZROKU){
            int kierunek = generator.nextInt(4);
            poczatekKrokuHelper(kierunek);
        }
        else{
            //4 mozliwosci sprawdzic?
            int yDziecka = this.getPos().getFirst();
            int xDziecka = this.getPos().getSecond();
            int yMikolaja = mikolaj.getPos().getFirst();
            int xMikolaja = mikolaj.getPos().getSecond();
            //0 gora, 1 prawo 2 dol 3 lewo
            //mozemy chodzic tylko manhatansko, wiec nie ma znaczenia czy pojdziemy w dol czy w lewo jesli mikolaj jest na poludniowy zachod
            // i tak przyblizymy sie o 1 niezaleznie od kierunku
            if(yMikolaja > yDziecka){
                poczatekKrokuHelper(0);
            }
            else if(yMikolaja < yDziecka){
                poczatekKrokuHelper(2);
            }
            else if(xMikolaja < xDziecka){
                poczatekKrokuHelper(3);
            }
            else{
                poczatekKrokuHelper(1);
            }
        }
    }

}
