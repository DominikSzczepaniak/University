package lista9.lista9.obiekty;

public class ObiektNaPlanszy {
    public int szybkosc;
    Para pos;
    boolean wTrakcieKroku = false;
    public int kierunekStrzalki = -1; //0 gora, 1 prawo, 2 dol, 3 lewo
    //do ukladu graficznego zeby bylo wiadomo w ktora strone idzie dziecko (dla mikolaja nie rysuj)
    int progresKroku = 0;
    Para dokadKrok = null;
    public int odleglosc = 0; //odleglosc od ostatniego zasniecia, jesli odleglosc==ZASIEG_ZMECZENIA to spi na CZAS_PRZERWY
    public void wykonajProgresKroku(){
        if(!wTrakcieKroku){
            return;
        }
        progresKroku++;
        if(progresKroku == szybkosc){
            kierunekStrzalki = -1;
            wTrakcieKroku = false;
            progresKroku = 0;
            setPos(dokadKrok);
            dokadKrok = null;
            odleglosc++;
        }
    }

    public void zacznijKrok(Para kierunek){
        dokadKrok = new Para(this.getPos().getFirst() + kierunek.getFirst(), this.getPos().getSecond()+kierunek.getSecond());
        wTrakcieKroku = true;
        progresKroku = 0;
        if(kierunek.getFirst() == 1){
            kierunekStrzalki = 0;
        }
        else if(kierunek.getFirst() == -1){
            kierunekStrzalki = 2;
        }
        else if(kierunek.getSecond() == 1){
            kierunekStrzalki = 1;
        }
        else{
            kierunekStrzalki = 3;
        }
    }

    public void poczatekKrokuHelper(int kierunek){
        kierunekStrzalki = kierunek;
        switch(kierunek){
            case 0:
                zacznijKrok(new Para(1, 0));
                break;
            case 1:
                zacznijKrok(new Para(0, 1));
                break;
            case 2:
                zacznijKrok(new Para(-1, 0));
                break;
            case 3:
                zacznijKrok(new Para(0, -1));
                break;
        }
    }

    public Para getPos() {
        return pos;
    }

    public void setPos(Para pos) {
        this.pos = pos;
    }
}
