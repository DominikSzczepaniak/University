package lista3_klasy;

public class Punkt {
    public Punkt(double a, double b){
        y = a;
        x = b;
    }

    public static boolean wspolliniowe(Punkt a, Punkt b, Punkt c){
        // y = qx + c
        // a = (y1, x1)
        // b = (y2, x2)
        // y1 = qx1 + r
        // y2 = qx2 + r
        // y1-y2 = q(x1-x2)
        // q = (y1-y2) / (x1 - x2)
        // r = y1 - qx1
        double q1 = (a.y - b.y) / (a.x - b.x);
        double r1 = a.y - q1 * a.x;
        double q2 = (a.y - c.y) / (a.x - c.x);
        double r2 = a.y - q2 * a.x;
        if(q1 == q2 && r1 == r2){
            return true;
        }
        return false;
    }

    public void obroc(Punkt p, double kat){
        double radiany = Math.toRadians(kat);
        double cosinus = Math.cos(radiany);
        double sinus = Math.sin(radiany);
        double xDiff = x - p.getX();
        double yDiff = y - p.getY();

        double newX = xDiff * cosinus - yDiff * sinus + p.getX();
        double newY = xDiff * sinus + yDiff * cosinus + p.getY();

        x = newX;
        y = newY;
    }

    public void przesun(Wektor v){
        this.y += v.getDy();
        this.x += v.getDx();
    }

    public void odbij(Prosta p) throws Exception {
        //musimy znalezc prosta prostopadla to prostej p i wyznaczyc jej wzor tak, zeby przechodzila przez Punkt ktory podaje
        //na tej podstawie moge obliczyc odleglosc od prostej P
        //teraz jesli mamy juz odleglosc od prostej, to musi ona lezec
        Prosta prostopadla = p.prostaProstopadlaPrzezPunkt(this);
        Punkt przeciecie = prostopadla.przeciecieProstych(p);
        if(przeciecie == null){
            throw new Exception("Prosta nie moze byc rownolegla ");
        }
        Wektor this_przeciecie = Wektor.WektorMiedzyPunktami(this, przeciecie); //ERROR HERE
        Wektor odwrotny = new Wektor(-this_przeciecie.getDy(), -this_przeciecie.getDx());
        przeciecie.przesun(odwrotny);
        this.x = przeciecie.getX();
        this.y = przeciecie.getY();

    }
    public void wypisz(){
        System.out.println(this.y + " " + this.x);
    }
    public double getY(){
        return this.y;
    }

    public double getX(){
        return this.x;
    }
    public void setX(double x){
        this.x = x;
    }
    public void setY(double y){
        this.y = y;
    }

    private double y;
    private double x;
}
