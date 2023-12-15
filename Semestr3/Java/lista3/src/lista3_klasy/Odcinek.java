package lista3_klasy;

public class Odcinek {
    public Odcinek(Punkt jeden, Punkt dwa){
        if(jeden == dwa){
            throw new IllegalArgumentException("Aby stworzyć odcinek trzeba podać dwa różne punkty");
        }
        else{
            a = jeden;
            b = dwa;
        }
    }
    public void obroc(Punkt p, double kat){
        double radiany = Math.toRadians(kat);
        double cosinus = Math.cos(radiany);
        double sinus = Math.sin(radiany);
        Punkt[] punkty = {a, b};
        obracaniePuntkow(p, cosinus, sinus, punkty);
    }

    static void obracaniePuntkow(Punkt p, double cosinus, double sinus, Punkt[] punkty) {
        for(Punkt c : punkty){
            if(c == p){
                continue;
            }
            double xDiff = c.getX() - p.getX();
            double yDiff = c.getY() - p.getY();

            double newX = xDiff * cosinus - yDiff*sinus + p.getX();
            double newY = xDiff * sinus + yDiff * cosinus + p.getY();

            c.setX(newX);
            c.setY(newY);

        }
    }

    public void przesun(Wektor v){
        a.przesun(v);
        b.przesun(v);
    }

    public void odbij(Prosta r) throws Exception {
        this.a.odbij(r);
        this.b.odbij(r);
    }
    public void wypisz(){
        this.a.wypisz();
        this.b.wypisz();
    }
    private Punkt a;
    private Punkt b;
}
