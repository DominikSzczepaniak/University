import java.io.Serializable;

class Elektronika extends Przedmiot implements Serializable {
    protected String producent;
    protected String kategoria;
    protected String zastosowanie;

    public Elektronika(String nazwa, int waga, double cena, String producent, String kategoria, String zastosowanie) {
        super(nazwa, waga, cena);
        this.producent = producent;
        this.kategoria = kategoria;
        this.zastosowanie = zastosowanie;
    }

    @Override
    public String toString() {
        return super.toString() + " Producent: " + producent + " Kategoria: " + kategoria + " Zastosowanie: " + zastosowanie;
    }
}