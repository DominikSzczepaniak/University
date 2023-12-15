package lista3_klasy;


public class Wektor {
    public Wektor(double jeden, double dwa){
        this.dy = jeden;
        this.dx = dwa;
    }
    static public Wektor WektorMiedzyPunktami(Punkt a, Punkt b){
        return new Wektor(a.getY() - b.getY(), a.getX() - b.getX());
    }
    static public Wektor skladanie(Wektor a, Wektor b){
        return new Wektor(a.getDy() + b.getDy(), a.getDx() + b.getDx());
    }

    public double getDx() {
        return dx;
    }

    public double getDy() {
        return dy;
    }
    public void wypisz(){
        System.out.println(this.dy + " " + this.dx);
    }

    private double dy;
    private double dx;
}

