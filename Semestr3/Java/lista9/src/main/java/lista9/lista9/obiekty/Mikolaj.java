package lista9.lista9.obiekty;

public class Mikolaj extends ObiektNaPlanszy{
    private int iloscPaczek;

    public Mikolaj(int iloscPaczek){
        this.iloscPaczek = iloscPaczek;
        szybkosc = 1;
    }

    public int getIloscPaczek() {
        return iloscPaczek;
    }

    public void setIloscPaczek(int iloscPaczek) {
        this.iloscPaczek = iloscPaczek;
    }

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
            odleglosc++;
        }
    }
}
