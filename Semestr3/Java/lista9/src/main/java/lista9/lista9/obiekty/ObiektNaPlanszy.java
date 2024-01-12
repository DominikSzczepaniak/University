package lista9.lista9.obiekty;

public class ObiektNaPlanszy {
    private int szybkosc;
    Para pos;
    boolean wTrakcieKroku = false;
    int kierunekStrzalki = -1; //0 gora, 1 prawo, 2 dol, 3 lewo
    //do ukladu graficznego zeby bylo wiadomo w ktora strone idzie dziecko (dla mikolaja nie rysuj)
    int progresKroku = 0;
    Para dokadKrok = null;
    public void wykonajProgresKroku(){
        if(!wTrakcieKroku){
            return;
        }
        progresKroku++;
        if(progresKroku == szybkosc){
            wTrakcieKroku = false;
            progresKroku = 0;
            setPos(dokadKrok);
            dokadKrok = null;
        }
    }

    public void zacznijKrok(Para dokad, Para kierunek){
        dokadKrok = dokad;
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

    public Para getPos() {
        return pos;
    }

    public void setPos(Para pos) {
        this.pos = pos;
    }
}
