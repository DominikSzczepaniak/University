package lista3_klasy;

public class Prosta {
    // Konstruktor
    public Prosta(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    // Metoda zwracająca prostopadłą prostą przechodzącą przez punkt P
    public Prosta prostaProstopadlaPrzezPunkt(Punkt p) {
        // Wzór prostej prostopadłej - a * a2 + b * b2 = -c
        // a, b, c to współczynniki prostej, a2, b2 to współrzędne wektora prostopadłego

        double a2 = -this.b;
        double b2 = this.a;
        double c2 = (-a2*p.getX()-b2*p.getY());

        return new Prosta(a2, b2, c2);
    }

    // Metoda obliczająca punkt przecięcia dwóch prostych
    public Punkt przeciecieProstych(Prosta p){
        if(this.getA() * p.getB() - p.getA() * this.getB() == 0){
            return null;
        }
        double x = (this.getB()*p.getC() - p.getB()*this.getC()) / (this.getA()*p.getB() - p.getA()*this.getB());
        double y = (p.getA()*this.getC()-this.getA()*p.getC()) / (this.getA()*p.getB() - p.getA()*this.getB());
        return new Punkt(y, x);
    }
    static public double odlegloscOdPunktu(Prosta r, Punkt p){
        // Wtedy odleglosc = |Ax0 + By0 + C| / sqrt(A*A + B*B)
        double A = r.getA();
        double B = r.getB();
        double C = r.getC();
        double x0 = p.getX();
        double y0 = p.getY();
        return Math.abs(A * x0 + B * y0 + C) / Math.sqrt(A*A + B*B);
    }
    public double getA(){
        return a;
    }

    public double getB() {
        return b;
    }

    public double getC() {
        return c;
    }
    public void wypisz(){
        System.out.println(this.a + " " + this.b + " " + this.c);
    }

    private double a;
    private double b;
    private double c;
}

