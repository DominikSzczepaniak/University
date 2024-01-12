package lista9.lista9.obiekty;

public class Mikolaj extends ObiektNaPlanszy {
    private int iloscPaczek;
    private int y;
    private int x;

    public Mikolaj(int iloscPaczek){
        this.iloscPaczek = iloscPaczek;
    }

    public void polozPrezent(){

    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}
